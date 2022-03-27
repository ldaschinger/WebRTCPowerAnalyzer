__author__ = "Lukas Daschinger"
__version__ = "1.0.1"
__maintainer__ = "Lukas Daschinger"
__email__ = "ldaschinger@student.ethz.ch"

import getopt
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import re
from ast import literal_eval
import numpy as np
import json



def analyzeWebRTCStats(filepath, samplesFromTheBackN = 60, toSampleN=60):
    # print head including sampling interval
    with open(filepath) as myfile:
        head = [next(myfile) for x in range(6)]
    # print(head, "\n")

    # if want to exclude N first samples. default value is recommended at 4 with a normal bitrates ramp up
    # fromSampleN = 5
    # toSampleN = 54 # one sample every second taken


    callIdInboundRegex = re.compile(r'RTCInboundRTPVideoStream_(\d+)-\[bytesReceived_in_bits/s\]') #RTCInboundRTPVideoStream_3703603861-[bytesReceived_in_bits/s]
    callIdOutboundRegex = re.compile(r'RTCOutboundRTPVideoStream_(\d+)-\[bytesSent_in_bits/s\]')  # RTCOutboundRTPVideoStream_506976331-[bytesSent_in_bits/s]
    pairIdRegex = re.compile(r'RTCIceCandidatePair_([a-zA-Z0-9+/_]+)*-currentRoundTripTime')  #RTCIceCandidatePair_TvloZs3f_YAKLS8Og-currentRoundTripTime
    topLevelIdRegex = re.compile(r'"(\d+)-(\d+)": \{')

    callIdInbound = 0
    callIdOutbound = 0
    pairId = ''
    topId = ''

    for i, line in enumerate(open(filepath)):
        for match in re.finditer(callIdInboundRegex, line):
            # print('Found call ID on line %s: %s' % (i + 1, match.group(1)))
            callIdInbound = match.group(1)
        for match in re.finditer(callIdOutboundRegex, line):
            # print('Found call ID on line %s: %s' % (i + 1, match.group(1)))
            callIdOutbound = match.group(1)
        for match in re.finditer(pairIdRegex, line):
            # print('Found pair ID on line %s: %s' % (i + 1, match.group(1)))
            pairId = match.group(1)
        for match in re.finditer(topLevelIdRegex, line):
            # print('Found pair ID on line %s: %s-%s' % (i + 1, match.group(1), match.group(2)))
            topId = match.group(1) + '-' + match.group(2)
            # since we do a loop only the last topId is taken which is what we want


    # Opening JSON file
    print(filepath)
    f = open(filepath)
    # returns JSON object as a dictionary
    data = json.load(f)

    """
    JSON structure:
        getUserMedia[]
        PeerConnections{}
          10-1{} - can be in here
          10-2{} - or here
          8-4{} - or here
    """


    stringBitsPerSecReceived = 'RTCInboundRTPVideoStream_' + callIdInbound + '-[bytesReceived_in_bits/s]'
    stringQpSumPerFrame = 'RTCInboundRTPVideoStream_' + callIdInbound + '-[qpSum/framesDecoded]'
    stringFps = 'RTCInboundRTPVideoStream_' + callIdInbound + '-framesPerSecond'
    stringFrameWidth = 'RTCInboundRTPVideoStream_' + callIdInbound + '-frameWidth'
    stringFrameHeight = 'RTCInboundRTPVideoStream_' + callIdInbound + '-frameHeight'
    stringJitter = 'RTCInboundRTPVideoStream_' + callIdInbound + '-jitter'
    stringJitterBufferDelay = 'RTCInboundRTPVideoStream_' + callIdInbound + '-[jitterBufferDelay/jitterBufferEmittedCount_in_ms]'
    stringRTT = 'RTCIceCandidatePair_' + pairId + '-currentRoundTripTime'

    #for other dir
    stringAvailableBW = 'RTCIceCandidatePair_' + pairId + '-availableOutgoingBitrate' # RTCIceCandidatePair_0VsWsvS0_4s6VQfkL-availableOutgoingBitrate
    stringRemoteInboundJitter = 'RTCRemoteInboundRtpVideoStream_' + callIdOutbound + '-jitter'   # "RTCRemoteInboundRtpVideoStream_506976331-jitter"
    stringBitsPerSecSent = 'RTCOutboundRTPVideoStream_' + callIdOutbound + '-[bytesSent_in_bits/s]'   # RTCOutboundRTPVideoStream_506976331-[bytesSent_in_bits/s]
    stringQpSumPerFrameOutbound = 'RTCOutboundRTPVideoStream_' + callIdOutbound + '-[qpSum/framesEncoded]' # "RTCOutboundRTPVideoStream_506976331-[qpSum/framesEncoded]"


    returnDict = {
        "bitsPerSec": 0,
        "qpSumPerFrame": 0,
        "fps": 0,
        "width": 0,
        "height": 0,
        "pixels": 0,
        "jitter": 0,
        "jitterBufDelay": 0,
        "RTT": 0,
        "AvailableBW": 0,
        "RemoteInboundJitter": 0,
        "bitsPerSecSent": 0,
        "qpSumPerFrameSent": 0,

        "jitterMax": 0,

        "bitsPerSecVar": 0,
        "qpSumPerFrameVar": 0,
        "fpsVar": 0,
        "widthVar": 0,
        "heightVar": 0,
        "pixelsVar": 0,
        "jitterVar": 0,
        "jitterBufDelayVar": 0,
        "RTTVar": 0,
        "AvailableBWVar": 0,
        "RemoteInboundJitterVar": 0,
        "bitsPerSecSentVar": 0,
        "qpSumPerFrameSentVar": 0,
    }

    value = data['PeerConnections'][topId]['stats'][stringAvailableBW]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["AvailableBW"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["AvailableBWVar"] = npArray[-samplesFromTheBackN:].var()

    value = data['PeerConnections'][topId]['stats'][stringRemoteInboundJitter]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["RemoteInboundJitter"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["RemoteInboundJitterVar"] = npArray[-samplesFromTheBackN:].var()

    value = data['PeerConnections'][topId]['stats'][stringBitsPerSecSent]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["bitsPerSecSent"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["bitsPerSecSentVar"] = npArray[-samplesFromTheBackN:].var()

    value = data['PeerConnections'][topId]['stats'][stringQpSumPerFrameOutbound]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["qpSumPerFrameSent"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["qpSumPerFrameSentVar"] = npArray[-samplesFromTheBackN:].var()







    value = data['PeerConnections'][topId]['stats'][stringBitsPerSecReceived]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["bitsPerSec"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["bitsPerSecVar"] = npArray[-samplesFromTheBackN:].var()


    value = data['PeerConnections'][topId]['stats'][stringQpSumPerFrame]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["qpSumPerFrame"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["qpSumPerFrameVar"] = npArray[-samplesFromTheBackN:].var()


    value = data['PeerConnections'][topId]['stats'][stringFps]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["fps"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["fpsVar"] = npArray[-samplesFromTheBackN:].var()



    value = data['PeerConnections'][topId]['stats'][stringFrameWidth]['values']
    array = literal_eval(value)
    npArrayWidth = np.array(array)
    returnDict["width"] = npArrayWidth[-samplesFromTheBackN:].mean()
    returnDict["widthVar"] = npArrayWidth[-samplesFromTheBackN:].var()


    value = data['PeerConnections'][topId]['stats'][stringFrameHeight]['values']
    array = literal_eval(value)
    npArrayHeight = np.array(array)
    returnDict["height"] = npArrayHeight[-samplesFromTheBackN:].mean()
    returnDict["heightVar"] = npArrayHeight[-samplesFromTheBackN:].var()

    returnDict["pixels"] = np.mean(np.multiply(npArrayHeight[-samplesFromTheBackN:], npArrayWidth[-samplesFromTheBackN:]))
    returnDict["pixelsVar"] = np.var(np.multiply(npArrayHeight[-samplesFromTheBackN:], npArrayWidth[-samplesFromTheBackN:]))


    value = data['PeerConnections'][topId]['stats'][stringJitter]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["jitter"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["jitterVar"] = npArray[-samplesFromTheBackN:].var()
    returnDict["jitterMax"] = npArray[-samplesFromTheBackN:].max()



    value = data['PeerConnections'][topId]['stats'][stringJitterBufferDelay]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["jitterBufDelay"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["jitterBufDelayVar"] = npArray[-samplesFromTheBackN:].var()


    value = data['PeerConnections'][topId]['stats'][stringRTT]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    returnDict["RTT"] = npArray[-samplesFromTheBackN:].mean()
    returnDict["RTTVar"] = npArray[-samplesFromTheBackN:].var()

    # Closing file
    f.close()

    # print("#", end="", flush=True)
    return returnDict