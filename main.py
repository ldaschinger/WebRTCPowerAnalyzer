"""
Extracts various values from Keysight Data Logger *.csv file like
average current, average power, cumulative sum of energy used

Possibility to plot the current and energy consumption with matplotlib
"""

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

def analyzeWebRTCStats(filepath, fromSampleN=5, toSampleN=54):
    # print head including sampling interval
    with open(filepath) as myfile:
        head = [next(myfile) for x in range(6)]
    # print(head, "\n")

    # if want to exclude N first samples. default value is recommended at 4 with a normal bitrates ramp up
    # fromSampleN = 5
    # toSampleN = 54 # one sample every second taken


    callIdRegex = re.compile(r'RTCInboundRTPVideoStream_(\d+)-\[bytesReceived_in_bits/s\]') #RTCInboundRTPVideoStream_3703603861-[bytesReceived_in_bits/s]
    pairIdRegex = re.compile(r'RTCIceCandidatePair_([a-zA-Z0-9+/_]+)*-currentRoundTripTime')  #RTCIceCandidatePair_TvloZs3f_YAKLS8Og-currentRoundTripTime
    topLevelIdRegex = re.compile(r'"(\d+)-(\d+)": \{')

    callId = 0
    pairId = ''
    topId = ''

    for i, line in enumerate(open(filepath)):
        for match in re.finditer(callIdRegex, line):
            # print('Found call ID on line %s: %s' % (i + 1, match.group(1)))
            callId = match.group(1)
        for match in re.finditer(pairIdRegex, line):
            # print('Found pair ID on line %s: %s' % (i + 1, match.group(1)))
            pairId = match.group(1)
        for match in re.finditer(topLevelIdRegex, line):
            # print('Found pair ID on line %s: %s-%s' % (i + 1, match.group(1), match.group(2)))
            topId = match.group(1) + '-' + match.group(2)
            # since we do a loop only the last topId is taken which is what we want


    # Opening JSON file
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


    stringBitsPerSecReceived = 'RTCInboundRTPVideoStream_' + callId + '-[bytesReceived_in_bits/s]'
    stringQpSumPerFrame = 'RTCInboundRTPVideoStream_' + callId + '-[qpSum/framesDecoded]'
    stringFps = 'RTCInboundRTPVideoStream_' + callId + '-framesPerSecond'
    stringFrameWidth = 'RTCInboundRTPVideoStream_' + callId + '-frameWidth'
    stringFrameHeight = 'RTCInboundRTPVideoStream_' + callId + '-frameHeight'
    stringJitter = 'RTCInboundRTPVideoStream_' + callId + '-jitter'
    stringJitterBufferDelay = 'RTCInboundRTPVideoStream_' + callId + '-[jitterBufferDelay/jitterBufferEmittedCount_in_ms]'
    stringRTT = 'RTCIceCandidatePair_' + pairId + '-currentRoundTripTime'

    returnDict = {
        "bitsPerSec": 0,
        "qpSumPerFrame": 0,
        "width": 0,
        "height": 0,
        "jitter": 0,
        "jitterBufDelay": 0,
        "RTT": 0,
    }

    value = data['PeerConnections'][topId]['stats'][stringBitsPerSecReceived]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    print(str(npArray[fromSampleN:].mean()))
    returnDict["bitsPerSec"] = npArray[fromSampleN:].mean()

    value = data['PeerConnections'][topId]['stats'][stringQpSumPerFrame]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["qpSumPerFrame"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringFps]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["fps"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringFrameWidth]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["width"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringFrameHeight]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["height"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringJitter]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["jitter"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringJitterBufferDelay]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["jitterBufDelay"] = npArray[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringRTT]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["RTT"] = npArray[fromSampleN:].mean()

    # Closing file
    f.close()

    return returnDict


def analyzeTestCustom(folderpath, bitrate, res1, fps1, codec1, res2="null", fps2="null", codec2="null",
                      res3="null", fps3="null", codec3="null", res4="null", fps4="null", codec4="null",
                      res5="null", fps5="null", codec5="null"):

    requests = [dict() for x in range(5)]
    requests[0] = {"res": res1, "fps": fps1, "codec": codec1}
    requests[1] = {"res": res2, "fps": fps2, "codec": codec2}
    requests[2] = {"res": res3, "fps": fps3, "codec": codec3}
    requests[3] = {"res": res4, "fps": fps4, "codec": codec4}
    requests[4] = {"res": res5, "fps": fps5, "codec": codec5}

    folderpaths = []
    for i in range(5):
        folderpaths.append(folderpath + requests[i].get("codec") + "/" + bitrate + "/" + bitrate + requests[i].get("res") + requests[i].get("fps"))

    bitsPerSecMeans = [[0 for x in range(0)] for y in range(5)]
    qpSumPerFrameMeans = [[0 for x in range(0)] for y in range(5)]
    widthMeans = [[0 for x in range(0)] for y in range(5)]
    heightMeans = [[0 for x in range(0)] for y in range(5)]
    jitterMeans = [[0 for x in range(0)] for y in range(5)]
    jitterBufDelayMeans = [[0 for x in range(0)] for y in range(5)]
    RTTMeans = [[0 for x in range(0)] for y in range(5)]

    for i in range(5):
        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[i].get("res") != "null":
            for item in os.listdir(folderpaths[i]):
                name, extension = os.path.splitext(item)
                # if there is no extension it is a folder
                if extension == "" and item != ".DS_Store":
                    statsDict = analyzeWebRTCStats(folderpaths[i] + "/" + item + "/" + "webrtc_internals_dump.txt", fromSampleN=5, toSampleN=54)
                    bitsPerSecMeans[i].append(statsDict["bitsPerSec"])
                    qpSumPerFrameMeans[i].append(statsDict["qpSumPerFrame"])
                    widthMeans[i].append(statsDict["width"])
                    heightMeans[i].append(statsDict["height"])
                    jitterMeans[i].append(statsDict["jitter"])
                    jitterBufDelayMeans[i].append(statsDict["jitterBufDelay"])
                    RTTMeans[i].append(statsDict["RTT"])


    npbitsPerSecMeans = [np.empty([5]) for x in range(5)]
    npqpSumPerFrameMeans = [np.empty([5]) for x in range(5)]
    npwidthMeans = [np.empty([5]) for x in range(5)]
    npheightMeans = [np.empty([5]) for x in range(5)]
    npjitterMeans = [np.empty([5]) for x in range(5)]
    npjitterBufDelayMeans = [np.empty([5]) for x in range(5)]
    npRTTMeans = [np.empty([5]) for x in range(5)]

    for i in range(5):
        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[i].get("res") != "null":
            npbitsPerSecMeans[i] = np.asarray(bitsPerSecMeans[i])
            npqpSumPerFrameMeans[i] = np.asarray(qpSumPerFrameMeans[i])
            npwidthMeans[i] = np.asarray(widthMeans[i])
            npheightMeans[i] = np.asarray(heightMeans[i])
            npjitterMeans[i] = np.asarray(jitterMeans[i])
            npjitterBufDelayMeans[i] = np.asarray(jitterBufDelayMeans[i])
            npRTTMeans[i] = np.asarray(RTTMeans[i])

    returnedDict = {
        "bitsPerSec": npbitsPerSecMeans,
        "qpSumPerFrame": npqpSumPerFrameMeans,
        "width": npwidthMeans,
        "height": npheightMeans,
        "jitter": npjitterMeans,
        "jitterBufDelay": npjitterBufDelayMeans,
        "RTT": npRTTMeans,
        "dictlist": requests
    }

    return returnedDict


    # for i in range(5):
    #     # if we have varying number of tests and therefore .csv files available we must find all in the folder
    #     if dictlist[i].get("res") != "null":
    #         print(str(format(npbitsPerSecMeans[i].mean(), ".2f")) + " " + str(format(npbitsPerSecMeans[i].std(), ".2f")) + " " + str(format(npbitsPerSecMeans[i].std(), ".2f")) + "  ", end="", flush=True)
    # print("\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folderpath",
                        required=True,
                        default=None,
                        help="Path to target CSV file folder")

    args = parser.parse_args()

    """
    directory structure:
    folderpath
        H264/VP8
            folderpath_small/large/auto
                dlog1.csv/dlog2.csv/dlog3.csv/dlog4.csv/...
    """

    dictsBitrates = []

    # 30 fps tests
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600",
                      res1="_small_", fps1="30", codec1="H264",
                      res2="_large_", fps2="30", codec2="H264",
                      res3="_auto_", fps3="30", codec3="H264"))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900",
                      res1="_small_", fps1="30", codec1="H264",
                      res2="_large_", fps2="30", codec2="H264",
                      res3="_auto_", fps3="30", codec3="H264"))
    # analyzeTestCustom(args.folderpath, bitrate="900",
    #                   res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264",
    #                   res3="_auto_", fps3="30", codec3="H264")

    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["bitsPerSec"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    # # VP8 tests
    # analyzeTestCustom(args.folderpath, bitrate="900",
    #                   res1="_small_", fps1="30", codec1="VP8",
    #                   res2="_large_", fps2="30", codec2="VP8",
    #                   res3="_auto_", fps3="30", codec3="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="1800",
    #                   res1="_small_", fps1="30", codec1="VP8",
    #                   res2="_large_", fps2="30", codec2="VP8",
    #                   res3="_auto_", fps3="30", codec3="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="4000",
    #                   res1="_small_", fps1="30", codec1="VP8",
    #                   res2="_large_", fps2="30", codec2="VP8",
    #                   res3="_auto_", fps3="30", codec3="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="6000",
    #                   res1="_small_", fps1="30", codec1="VP8",
    #                   res2="_large_", fps2="30", codec2="VP8",
    #                   res3="_auto_", fps3="30", codec3="VP8")

    # VP8 vs H264 tests
    # analyzeTestCustom(args.folderpath, bitrate="900",
    #                   res1="_small_", fps1="30", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="VP8",
    #                   res3="_large_", fps3="30", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="1800",
    #                   res1="_small_", fps1="30", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="VP8",
    #                   res3="_large_", fps3="30", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="4000",
    #                   res1="_small_", fps1="30", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="VP8",
    #                   res3="_large_", fps3="30", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="VP8")
    # analyzeTestCustom(args.folderpath, bitrate="6000",
    #                   res1="_small_", fps1="30", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="VP8",
    #                   res3="_large_", fps3="30", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="VP8")

    # # 15fps vs 30fps H264
    # analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")
    # analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                   res4="_large_", fps4="30", codec4="H264")