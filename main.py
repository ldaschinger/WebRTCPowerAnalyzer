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
    }

    value = data['PeerConnections'][topId]['stats'][stringAvailableBW]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["AvailableBW"] = npArray[fromSampleN:].mean()

    value = data['PeerConnections'][topId]['stats'][stringRemoteInboundJitter]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["RemoteInboundJitter"] = npArray[fromSampleN:].mean()

    value = data['PeerConnections'][topId]['stats'][stringBitsPerSecSent]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["bitsPerSecSent"] = npArray[fromSampleN:].mean()

    value = data['PeerConnections'][topId]['stats'][stringQpSumPerFrameOutbound]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["qpSumPerFrameSent"] = npArray[fromSampleN:].mean()






    value = data['PeerConnections'][topId]['stats'][stringBitsPerSecReceived]['values']
    array = literal_eval(value)
    npArray = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
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
    npArrayWidth = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["width"] = npArrayWidth[fromSampleN:].mean()


    value = data['PeerConnections'][topId]['stats'][stringFrameHeight]['values']
    array = literal_eval(value)
    npArrayHeight = np.array(array)
    # print(str(npArray[fromSampleN:].mean()))
    returnDict["height"] = npArrayHeight[fromSampleN:].mean()

    returnDict["pixels"] = np.mean(np.multiply(npArrayHeight[fromSampleN:], npArrayWidth[fromSampleN:]))


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

    print("#", end="", flush=True)
    return returnDict


def analyzeTestCustom(folderpath, bitrate, res1, fps1, codec1, res2="null", fps2="null", codec2="null",
                      res3="null", fps3="null", codec3="null", res4="null", fps4="null", codec4="null",
                      res5="null", fps5="null", codec5="null", startSample=5):

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




    for i in range(5):
        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[i].get("res") != "null":
            for item in os.listdir(folderpaths[i]):
                name, extension = os.path.splitext(item)
                # if there is no extension it is a folder
                if extension == "" and item != ".DS_Store":
                    statsDict = analyzeWebRTCStats(folderpaths[i] + "/" + item + "/" + "webrtc_internals_dump.txt", fromSampleN=startSample, toSampleN=54)
                    bitsPerSecMeans[i].append(statsDict["bitsPerSec"])
                    qpSumPerFrameMeans[i].append(statsDict["qpSumPerFrame"])
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
                    qpSumPerFrameSentMeans[i].append(statsDict["qpSumPerFrameSent"])


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
        "dictlist": requests
    }

    return returnedDictTests

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


    ########################################  30 fps tests  ########################################
    # dictsBitrates = []
    # listBitratesStrings = ["300", "600", "900", "1300", "1800", "2700", "4000", "4750", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4750", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))




    ########################################  15 fps tests  ########################################
    # dictsBitrates = []
    # listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", startSample=20))




    # VP8 tests
    # dictsBitrates = []
    # listBitratesStrings = ["900", "1800", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", startSample=20))


    # # VP8 vs H264 tests
    # dictsBitrates = []
    # listBitratesStrings = ["900", "1800", "4000", "6000"]
    # # we fix the start sample to 20s which is a good time for ramp up
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", startSample=20))



    # # # 15fps vs 30fps H264
    # dictsBitrates = []
    # listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="600", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="900", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1300", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="1800", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="2700", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="4000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="6000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", startSample=20))


    # PC only
    dictsBitrates = []
    listBitratesStrings = ["480", "720", "1080", "720H264"]
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
                      res1="_480_", fps1="10", codec1="VP8",
                      res2="_480_", fps2="30", codec2="VP8", startSample=20))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
                      res1="_720_", fps1="10", codec1="VP8",
                      res2="_720_", fps2="30", codec2="VP8", startSample=20))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
                      res1="_1080_", fps1="10", codec1="VP8",
                      res2="_1080_", fps2="30", codec2="VP8", startSample=20))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate="nolimit",
                      res1="_720_", fps1="10", codec1="H264",
                      res2="_720_", fps2="30", codec2="H264", startSample=20))







    
    ################ Received Bitrate
    print("\nReceived Bitrate:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["bitsPerSec"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")





    ################ Sent bitrate
    print("Sent Bitrate:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["bitsPerSecSent"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ Available BW
    print("Available Bandwidth:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["AvailableBW"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")




    ################ qpSumPerFrame
    print("qpSumPerFrame:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["qpSumPerFrame"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ fps
    print("fps:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["fps"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ pixels
    print("pixels:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["pixels"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ width
    print("width:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["width"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

    ################ jitter
    print("jitter:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["jitter"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".5f")) + " " + str(
                    format(npArrayValue.std(), ".5f")) + " " + str(format(npArrayValue.std(), ".5f")) + "  ",
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
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".5f")) + " " + str(
                    format(npArrayValue.std(), ".5f")) + " " + str(format(npArrayValue.std(), ".5f")) + "  ",
                      end="", flush=True)
        print("\n")

    ################ qpSum/frames sent
    print("qpSumPerFrame Sent:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["qpSumPerFrameSent"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
        print("\n")

