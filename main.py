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

    print("#", end="", flush=True)
    return returnDict


def analyzeTestCustom(folderpath, bitrate, res1, fps1, codec1, res2="null", fps2="null", codec2="null",
                      res3="null", fps3="null", codec3="null", res4="null", fps4="null", codec4="null",
                      res5="null", fps5="null", codec5="null", nSamplesFromTheBackN=60):

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
    fpsMeans = [[0 for x in range(0)] for y in range(5)]
    widthMeans = [[0 for x in range(0)] for y in range(5)]
    heightMeans = [[0 for x in range(0)] for y in range(5)]
    pixelsMeans = [[0 for x in range(0)] for y in range(5)]
    jitterMeans = [[0 for x in range(0)] for y in range(5)]
    jitterBufDelayMeans = [[0 for x in range(0)] for y in range(5)]
    RTTMeans = [[0 for x in range(0)] for y in range(5)]
    availableBWMeans = [[0 for x in range(0)] for y in range(5)]
    remoteJitterMeans = [[0 for x in range(0)] for y in range(5)]
    bitsPerSecSentMeans = [[0 for x in range(0)] for y in range(5)]
    qpSumPerFrameSentMeans = [[0 for x in range(0)] for y in range(5)]

    CurrentMeans = [[0 for x in range(0)] for y in range(5)]

    jitterMax = [[0 for x in range(0)] for y in range(5)]

    # we want to calculate the variance of the average calculated from the tests
    # the formula is: stddev = sqrt(mean(variances)) = sqrt(sum(variances)/n)
    # https://stats.stackexchange.com/questions/168971/variance-of-an-average-of-random-variables
    bitsPerSecVars = [[0 for x in range(0)] for y in range(5)]
    qpSumPerFrameVars = [[0 for x in range(0)] for y in range(5)]
    fpsVars = [[0 for x in range(0)] for y in range(5)]
    widthVars = [[0 for x in range(0)] for y in range(5)]
    heightVars = [[0 for x in range(0)] for y in range(5)]
    pixelsVars = [[0 for x in range(0)] for y in range(5)]
    jitterVars = [[0 for x in range(0)] for y in range(5)]
    jitterBufDelayVars = [[0 for x in range(0)] for y in range(5)]
    RTTVars = [[0 for x in range(0)] for y in range(5)]
    availableBWVars = [[0 for x in range(0)] for y in range(5)]
    remoteJitterVars = [[0 for x in range(0)] for y in range(5)]
    bitsPerSecSentVars = [[0 for x in range(0)] for y in range(5)]
    qpSumPerFrameSentVars = [[0 for x in range(0)] for y in range(5)]



    for i in range(5):



        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[i].get("res") != "null":
            for item in os.listdir(folderpaths[i]):
                name, extension = os.path.splitext(item)

                if extension == ".csv":
                    CurrentMeans[i].append(analyzeLoggerData(folderpaths[i] + "/" + item))

                # if there is no extension it is a folder
                if extension == "" and item != ".DS_Store":
                    statsDict = analyzeWebRTCStats(folderpaths[i] + "/" + item + "/" + "webrtc_internals_dump.txt", samplesFromTheBackN=nSamplesFromTheBackN, toSampleN=54)
                    bitsPerSecMeans[i].append(statsDict["bitsPerSec"])
                    fpsMeans[i].append(statsDict["fps"])
                    widthMeans[i].append(statsDict["width"])
                    heightMeans[i].append(statsDict["height"])
                    pixelsMeans[i].append(statsDict["pixels"])
                    jitterMeans[i].append(statsDict["jitter"])
                    jitterBufDelayMeans[i].append(statsDict["jitterBufDelay"])
                    RTTMeans[i].append(statsDict["RTT"])
                    availableBWMeans[i].append(statsDict["AvailableBW"])
                    remoteJitterMeans[i].append(statsDict["RemoteInboundJitter"])
                    bitsPerSecSentMeans[i].append(statsDict["bitsPerSecSent"])
                    # depending on the codec we need to scale the qpSum differently
                    # max VP8 is 126, max H264 is 51
                    # https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpStreamStats/qpSum
                    # probably should not compare codecs directly!

                    jitterMax[i].append(statsDict["jitterMax"])

                    # sometimes _auto_ is also in the H264 folder so if we use auto we always have VP8
                    if requests[i].get("codec") == "H264" and requests[i].get("res") != "_auto_":
                        qpSumPerFrameMeans[i].append(statsDict["qpSumPerFrame"]/51*100)
                        qpSumPerFrameSentMeans[i].append(statsDict["qpSumPerFrameSent"]/51*100)
                    # if it's auto in H264 folder or in VP8 folder VP8 is being used
                    else:
                        qpSumPerFrameMeans[i].append(statsDict["qpSumPerFrame"]/127*100)
                        qpSumPerFrameSentMeans[i].append(statsDict["qpSumPerFrameSent"]/127*100)

                    bitsPerSecVars[i].append(statsDict["bitsPerSecVar"])
                    fpsVars[i].append(statsDict["fpsVar"])
                    widthVars[i].append(statsDict["widthVar"])
                    heightVars[i].append(statsDict["heightVar"])
                    pixelsVars[i].append(statsDict["pixelsVar"])
                    jitterVars[i].append(statsDict["jitterVar"])
                    jitterBufDelayVars[i].append(statsDict["jitterBufDelayVar"])
                    RTTVars[i].append(statsDict["RTTVar"])
                    availableBWVars[i].append(statsDict["AvailableBWVar"])
                    remoteJitterVars[i].append(statsDict["RemoteInboundJitterVar"])
                    bitsPerSecSentVars[i].append(statsDict["bitsPerSecSentVar"])

                    if requests[i].get("codec") == "H264" and requests[i].get("res") != "auto":
                        qpSumPerFrameVars[i].append(statsDict["qpSumPerFrameVar"]/51*100)
                        qpSumPerFrameSentVars[i].append(statsDict["qpSumPerFrameSentVar"]/51*100)
                    else:
                        qpSumPerFrameVars[i].append(statsDict["qpSumPerFrameVar"]/127*100)
                        qpSumPerFrameSentVars[i].append(statsDict["qpSumPerFrameSentVar"]/127*100)



    npbitsPerSecMeans = [np.empty([5]) for x in range(5)]
    npqpSumPerFrameMeans = [np.empty([5]) for x in range(5)]
    npfpsMeans = [np.empty([5]) for x in range(5)]
    npwidthMeans = [np.empty([5]) for x in range(5)]
    npheightMeans = [np.empty([5]) for x in range(5)]
    nppixelsMeans = [np.empty([5]) for x in range(5)]
    npjitterMeans = [np.empty([5]) for x in range(5)]
    npjitterBufDelayMeans = [np.empty([5]) for x in range(5)]
    npRTTMeans = [np.empty([5]) for x in range(5)]
    npAvailableBWMeans = [np.empty([5]) for x in range(5)]
    npRemoteJitterMeans = [np.empty([5]) for x in range(5)]
    npBitsPerSecSentMeans = [np.empty([5]) for x in range(5)]
    npqpSumPerFrameSentMeans = [np.empty([5]) for x in range(5)]

    npCurrentMeans = [np.empty([5]) for x in range(5)]

    npjitterMax = [np.empty([5]) for x in range(5)]

    npbitsPerSecVars = [np.empty([5]) for x in range(5)]
    npqpSumPerFrameVars = [np.empty([5]) for x in range(5)]
    npfpsVars = [np.empty([5]) for x in range(5)]
    npwidthVars = [np.empty([5]) for x in range(5)]
    npheightVars = [np.empty([5]) for x in range(5)]
    nppixelsVars = [np.empty([5]) for x in range(5)]
    npjitterVars = [np.empty([5]) for x in range(5)]
    npjitterBufDelayVars = [np.empty([5]) for x in range(5)]
    npRTTVars = [np.empty([5]) for x in range(5)]
    npAvailableBWVars = [np.empty([5]) for x in range(5)]
    npRemoteJitterVars = [np.empty([5]) for x in range(5)]
    npBitsPerSecSentVars = [np.empty([5]) for x in range(5)]
    npqpSumPerFrameSentVars = [np.empty([5]) for x in range(5)]



    for k in range(5):
        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[k].get("res") != "null":
            npbitsPerSecMeans[k] = np.asarray(bitsPerSecMeans[k])
            npqpSumPerFrameMeans[k] = np.asarray(qpSumPerFrameMeans[k])
            npfpsMeans[k] = np.asarray(fpsMeans[k])
            npwidthMeans[k] = np.asarray(widthMeans[k])
            npheightMeans[k] = np.asarray(heightMeans[k])
            nppixelsMeans[k] = np.asarray(pixelsMeans[k])
            npjitterMeans[k] = np.asarray(jitterMeans[k])
            npjitterBufDelayMeans[k] = np.asarray(jitterBufDelayMeans[k])
            npRTTMeans[k] = np.asarray(RTTMeans[k])
            npAvailableBWMeans[k] = np.asarray(availableBWMeans[k])
            npRemoteJitterMeans[k] = np.asarray(remoteJitterMeans[k])
            npBitsPerSecSentMeans[k] = np.asarray(bitsPerSecSentMeans[k])
            npqpSumPerFrameSentMeans[k] = np.asarray(qpSumPerFrameSentMeans[k])

            npbitsPerSecVars[k] = np.asarray(bitsPerSecVars[k])
            npqpSumPerFrameVars[k] = np.asarray(qpSumPerFrameVars[k])
            npfpsVars[k] = np.asarray(fpsVars[k])
            npwidthVars[k] = np.asarray(widthVars[k])
            npheightVars[k] = np.asarray(heightVars[k])
            nppixelsVars[k] = np.asarray(pixelsVars[k])
            npjitterVars[k] = np.asarray(jitterVars[k])
            npjitterBufDelayVars[k] = np.asarray(jitterBufDelayVars[k])
            npRTTVars[k] = np.asarray(RTTVars[k])
            npAvailableBWVars[k] = np.asarray(availableBWVars[k])
            npRemoteJitterVars[k] = np.asarray(remoteJitterVars[k])
            npBitsPerSecSentVars[k] = np.asarray(bitsPerSecSentVars[k])
            npqpSumPerFrameSentVars[k] = np.asarray(qpSumPerFrameSentVars[k])

            npCurrentMeans[k] = np.asarray(CurrentMeans[k])

            npjitterMax[k] = np.asarray(jitterMax[k])



    returnedDictTests = {
        "bitsPerSec": npbitsPerSecMeans,
        "qpSumPerFrame": npqpSumPerFrameMeans,
        "fps": npfpsMeans,
        "width": npwidthMeans,
        "height": npheightMeans,
        "pixels": nppixelsMeans,
        "jitter": npjitterMeans,
        "jitterBufDelay": npjitterBufDelayMeans,
        "RTT": npRTTMeans,
        "AvailableBW": npAvailableBWMeans,
        "RemoteInboundJitter": npRemoteJitterMeans,
        "bitsPerSecSent": npBitsPerSecSentMeans,
        "qpSumPerFrameSent": npqpSumPerFrameSentMeans,

        "bitsPerSecVar": npbitsPerSecVars,
        "qpSumPerFrameVar": npqpSumPerFrameVars,
        "fpsVar": npfpsVars,
        "widthVar": npwidthVars,
        "heightVar": npheightVars,
        "pixelsVar": nppixelsVars,
        "jitterVar": npjitterVars,
        "jitterBufDelayVar": npjitterBufDelayVars,
        "RTTVar": npRTTVars,
        "AvailableBWVar": npAvailableBWVars,
        "RemoteInboundJitterVar": npRemoteJitterVars,
        "bitsPerSecSentVar": npBitsPerSecSentVars,
        "qpSumPerFrameSentVar": npqpSumPerFrameSentVars,

        "jitterMax": npjitterMax,

        "current": npCurrentMeans,

        "dictlist": requests
    }

    return returnedDictTests

    # for i in range(5):
    #     # if we have varying number of tests and therefore .csv files available we must find all in the folder
    #     if dictlist[i].get("res") != "null":
    #         print(str(format(npbitsPerSecMeans[i].mean(), ".2f")) + " " + str(format(npbitsPerSecMeans[i].std(), ".2f")) + " " + str(format(npbitsPerSecMeans[i].std(), ".2f")) + "  ", end="", flush=True)
    # print("\n")










def analyzeLoggerData(filepath):
    with open(filepath) as myfile:
        head = [next(myfile) for x in range(6)]

    df = pd.read_csv(filepath, sep=",", skiprows=6)

    meanC = df['Curr avg 1'].mean()
    """
    Given that the voltage is relatively stable (normal stddev around 6mV) 
    we can look at the current stddev directly to get a good estimate of the power standard deviation
    If the voltage changes strongly together with the current we also have to consider power stddev
    """
    return meanC*1000


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


    ########################################  30 fps tests  ########################################
    # dictsBitrates = []
    # listBitratesStrings = ["300", "600", "900", "1300", "1800", "2700", "4000", "4750", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4750", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))




    ########################################  15 fps tests  ########################################
    # dictsBitrates = []
    # listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))




    # VP8 tests
    # dictsBitrates = []
    # listBitratesStrings = ["900", "1800", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))


    # # VP8 vs H264 tests
    # dictsBitrates = []
    # listBitratesStrings = ["900", "1800", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))



    # # # 15fps vs 30fps H264
    dictsBitrates = []
    listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="15", codec1="H264",
                                           res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
                                           res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))


    # PC only
    # dictsBitrates = []
    # listBitratesStrings = ["480", "720", "1080", "720H264"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_480_", fps1="10", codec1="VP8",
    #                   res2="_480_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_720_", fps1="10", codec1="VP8",
    #                   res2="_720_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_1080_", fps1="10", codec1="VP8",
    #                   res2="_1080_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_720_", fps1="10", codec1="H264",
    #                   res2="_720_", fps2="30", codec2="H264", nSamplesFromTheBackN=60))






    # # 3D plot
    # dictsBitratesSmall = []
    # dictsBitratesLarge = []
    # dictsBitratesAuto = []
    # # listBitratesStrings = ["480", "720", "1080", "720H264"]
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="300",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="600",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="900",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="1300",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="1800",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="2700",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="4000",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="4750",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate="6000",
    #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    #
    #
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="300",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="600",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="900",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="1300",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="1800",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="2700",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="4000",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="4750",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate="6000",
    #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    #
    #
    #
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="300",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="600",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="900",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="1300",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="1800",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="2700",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="4000",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="4750",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate="6000",
    #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
    #

    # Only set res and no bitrate limit
    # dictsBitrates = []
    # listBitratesStrings = ["360-720", "960-1440"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_360_", fps1="30", codec1="H264",
    #                   res2="_480_", fps2="30", codec2="H264",
    #                   res3="_600_", fps3="30", codec3="H264",
    #                   res4="_720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
    #                   res1="_960_", fps1="30", codec1="H264",
    #                   res2="_1080_", fps2="30", codec2="H264",
    #                   res3="_1440_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))

    # ################ 3D plot
    # # small jitter300 MOS300 power300 jitter600 ...
    # # large jitter300 MOS300 power300 jitter600 ...
    # # auto  jitter300 MOS300 power300 jitter600 ...
    #
    # npArrayMOSSmall = [2.2225, 2.4125, 3.18, 2.8175, 3.5375, 3.3075, 3.6, 3.0625, 3.62]
    # npArrayMOSLarge = [2.445,2.795,2.8725,3.505,3.435,3.525,3.1325,3.69,3.745 ]
    # npArrayMOSAuto = [2.46,2.5325,2.616,2.6375,2.9,3.38,3.4325,3.5375,3.605 ]
    #
    # # for small
    # print("\n 3D plot small:")
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesSmall)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayJitter = dictsBitratesSmall[i]["jitter"][j]
    #         npArrayCurrent = dictsBitratesSmall[i]["current"][j]
    #         npArrayCheck = dictsBitratesSmall[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayJitter.mean(), ".5f")) + " " + str(format(npArrayMOSSmall[i], ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    #     # print("\n")
    #
    #
    # # for large
    # print("\n 3D plot large:")
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesLarge)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayJitter = dictsBitratesLarge[i]["jitter"][j]
    #         npArrayCurrent = dictsBitratesLarge[i]["current"][j]
    #         npArrayCheck = dictsBitratesLarge[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayJitter.mean(), ".5f")) + " " + str(format(npArrayMOSLarge[i], ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    #     # print("\n")
    #
    # # for auto
    # print("\n 3D plot auto:")
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesAuto)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayJitter = dictsBitratesAuto[i]["jitter"][j]
    #         npArrayCurrent = dictsBitratesAuto[i]["current"][j]
    #         npArrayCheck = dictsBitratesAuto[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayJitter.mean(), ".5f")) + " " + str(format(npArrayMOSLarge[i], ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    #     # print("\n")





    # we want to calculate the variance of the average calculated from the tests
    # the formula is: stddev = sqrt(mean(variances)) = sqrt(sum(variances)/n)
    # https://stats.stackexchange.com/questions/168971/variance-of-an-average-of-random-variables

    ################ Received Bitrate
    print("\n\nCurrent:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["current"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")


    ################ Received Bitrate
    print("\n\nReceived Bitrate:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["bitsPerSec"][j]
            npArrayValueVar = dictsBitrates[i]["bitsPerSecVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")



    ################ Sent bitrate
    print("Sent Bitrate:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["bitsPerSecSent"][j]
            npArrayValueVar = dictsBitrates[i]["bitsPerSecSentVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ Available BW
    print("Available Bandwidth:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["AvailableBW"][j]
            npArrayValueVar = dictsBitrates[i]["AvailableBWVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")




    ################ qpSumPerFrame
    print("qpSumPerFrame Received:  ! percentage of 100 of max compression:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["qpSumPerFrame"][j]
            npArrayValueVar = dictsBitrates[i]["qpSumPerFrameVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ fps
    print("fps:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["fps"][j]
            npArrayValueVar = dictsBitrates[i]["fpsVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ pixels
    print("pixels:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["pixels"][j]
            npArrayValueVar = dictsBitrates[i]["pixelsVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ width
    print("width:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["width"][j]
            npArrayValueVar = dictsBitrates[i]["widthVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ jitter
    print("jitter:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["jitter"][j]
            npArrayValueVar = dictsBitrates[i]["jitterVar"][j]
            npArrayValueMax = dictsBitrates[i]["jitterMax"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".5f")) + " "
                      + str(format(np.sqrt(npArrayValueVar.mean()), ".5f")) + " "
                      + str(format(np.sqrt(npArrayValueVar.mean()), ".5f")) + "  "
                      + str(format(npArrayValueMax.max(), ".5f")) + "  ",
                      end="", flush=True)
        print("\n")

    ################ Remote jitter
    print("Remote jitter:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["RemoteInboundJitter"][j]
            npArrayValueVar = dictsBitrates[i]["RemoteInboundJitterVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".5f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".5f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".5f")) + "  ",
                      end="", flush=True)
        print("\n")

    ################ qpSum/frames sent
    print("qpSumPerFrame Sent ! percentage of 100 of max compression:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["qpSumPerFrameSent"][j]
            npArrayValueVar = dictsBitrates[i]["qpSumPerFrameSentVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
        print("\n")

