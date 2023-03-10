"""
Extracts various parameters from
 - .csv Power Analyzer file
 - WebRTC stats on WebApp side
 - WebRTC stats on SBc side
 - codec settings from the logcat trace
"""

__author__ = "Lukas Daschinger"
__version__ = "1.0.1"
__maintainer__ = "Lukas Daschinger"
__email__ = "ldaschinger@student.ethz.ch"


import os
import numpy as np

from MOSDictionnary import MOSDict
from logcatParser import analyzeWebRTCStatsCodecBitrate
from WebRTCWebAppParser import analyzeWebRTCStats
from powerParser import analyzeLoggerData



# 'top' function calling other parsers for all the traces
# a max of 5 test cases can be requested to be parsed and printed out
def analyzeTestCustom(folderpath,
                      bitrate1="null", bitrate2="null", bitrate3="null", bitrate4="null", bitrate5="null",
                      res1="null", fps1="null", codec1="null",
                      res2="null", fps2="null", codec2="null",
                      res3="null", fps3="null", codec3="null",
                      res4="null", fps4="null", codec4="null",
                      res5="null", fps5="null", codec5="null",
                      nSamplesFromTheBackN=60):

    if bitrate2 == "null" and bitrate3 == "null" and bitrate4 == "null" and bitrate4 == "null":
        bitrate2 = bitrate1
        bitrate3 = bitrate1
        bitrate4 = bitrate1
        bitrate5 = bitrate1


    # create array with the requested test parameters
    requests = [dict() for x in range(5)]
    requests[0] = {"bitrate":bitrate1, "res": res1, "fps": fps1, "codec": codec1}
    requests[1] = {"bitrate":bitrate2, "res": res2, "fps": fps2, "codec": codec2}
    requests[2] = {"bitrate":bitrate3, "res": res3, "fps": fps3, "codec": codec3}
    requests[3] = {"bitrate":bitrate4, "res": res4, "fps": fps4, "codec": codec4}
    requests[4] = {"bitrate":bitrate5, "res": res5, "fps": fps5, "codec": codec5}

    # define the exact folderpath for each test that should be analyzed
    folderpaths = []
    for i in range(5):
        folderpaths.append(folderpath + requests[i].get("codec") + "/" + requests[i].get("bitrate") + "/" + requests[i].get("bitrate") + requests[i].get("res") + requests[i].get("fps"))

    # create 2D array for test cases and each test run per test case
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
    CodecBitrateMeans = [[0 for x in range(0)] for y in range(5)]

    MOSValues = [0 for x in range(5)]

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


    # at max 5 different test cases are requested
    for i in range(5):
        # if we have varying number of tests and therefore .csv files available we must find all in the folder
        if requests[i].get("res") != "null":

            MOSValues[i] = MOSDict[requests[i].get("codec")][requests[i].get("bitrate")][requests[i].get("res")][
                                    requests[i].get("fps")]
            print(folderpaths[i])
            for item in os.listdir(folderpaths[i]):
                name, extension = os.path.splitext(item)

                if extension == ".csv":
                    CurrentMeans[i].append(analyzeLoggerData(folderpaths[i] + "/" + item))

                # if there is no extension it is a folder
                if extension == "" and item != ".DS_Store":

                    calculatedBitrate = analyzeWebRTCStatsCodecBitrate(folderpaths[i] + "/" + item + "/" + "logcat.txt")
                    #function returns zero if the bitrate was not in trace file. In this case it must not be calculated in average
                    if calculatedBitrate != 0:
                        CodecBitrateMeans[i].append(calculatedBitrate)

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

                    jitterMax[i].append(statsDict["jitterMax"])

                    # depending on the codec we need to scale the qpSum differently
                    # max VP8 is 126, max H264 is 51
                    # https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpStreamStats/qpSum
                    # probably should not compare codecs directly!

                    # sometimes _auto_ is also in the H264 folder so if we use auto we always have VP8
                    if requests[i].get("codec") == "H264" and requests[i].get("res") != "_auto_" and requests[i].get("res") != "_auto720_":
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

    npCodecBitrateMeans = [np.empty([5]) for x in range(5)]

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


    #convert to np array
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

            npCodecBitrateMeans[k] = np.asarray(CodecBitrateMeans[k])

            # npMOSValues[k] = np.asarray(MOSValues[k])

            npjitterMax[k] = np.asarray(jitterMax[k])



    ############## calculating the QoE based on jitter, fps etc. ##############

    # we want to scale the parameters all to the range 0-100
    # min and max correspond to the min and max values over all tests made
    MIN_JITTER = 0.004
    MAX_JITTER = 0.08
    DIFF_JITTER = 0.076

    MIN_FPS = 10
    MAX_FPS = 35
    DIFF_FPS = 25

    MIN_PIXEL = 75000
    MAX_PIXEL  = 5000000
    DIFF_PIXEL = 4925000

    MIN_TROUGHPT = 200000
    MAX_TROUGHPT = 6000000
    DIFF_TROUGHPT = 5800000

    MIN_CODECBIT = 200000
    MAX_CODECBIT = 6000000
    DIFF_CODECBIT = 5800000

    MIN_MOS = 2
    MAX_MOS = 4
    DIFF_MOS = 2

    SCALE_RANGE = 5

    npJitterScaled = np.empty([5])
    npFpsScaled = np.empty([5])
    npPixelScaled = np.empty([5])
    npThroughpScaled = np.empty([5])
    npCodecbitScaled = np.empty([5])
    npMOSScaled = np.empty([5])

    for k in range(5):
        # jitter scale must be reversed since lower means better
        npJitterScaled[k] = (MAX_JITTER - npjitterMeans[k].mean())/DIFF_JITTER*SCALE_RANGE
        npFpsScaled[k] = (npfpsMeans[k].mean() - MIN_FPS) / DIFF_FPS * SCALE_RANGE
        npPixelScaled[k] = (nppixelsMeans[k].mean() - MIN_PIXEL) / DIFF_PIXEL * SCALE_RANGE
        npThroughpScaled[k] = (npbitsPerSecMeans[k].mean() - MIN_TROUGHPT) / DIFF_TROUGHPT * SCALE_RANGE
        npCodecbitScaled[k] = (npCodecBitrateMeans[k].mean() - MIN_CODECBIT) / DIFF_CODECBIT * SCALE_RANGE
        npMOSScaled[k] = (MOSValues[k] - MIN_MOS) / DIFF_MOS * SCALE_RANGE

    npOverallScore = np.empty([5])


    # QoE network = 0.14*(0.55*J+0.07*T) + 0.81*(J*T)+0.04*((0.55*J+0.07*T)*(J*T))
    #             = 0.022 J^2 T + 0.0028 J T^2 + 0.81 J T + 0.077 J + 0.0098 T
    # QoE app     = 0.19*(0.26*BR+0.63*F+0.11*R)+0.49*(BR*F*R)+0.042*((BR*F*R)*(0.26*BR+0.63*F+0.11*R))
    #             = 0.01092 B^2 F R^3 + 0.02646 B F^2 R^2 + 0.00462 B F R^3 + 0.49 B F R^2 + 0.0494 B R + 0.1197 F + 0.0209 R

    # QoE total   = 0.38*nw + 0.23*app
    #             = 0.00836 J^2 T + 0.001064 J T^2 + 0.3078 J T + 0.02926 J + 0.003724 T +
    #               0.0025116 B^2 F R^3 + 0.0060858 B F^2 R^2 + 0.0010626 B F R^3 + 0.1127 B F R^2 + 0.011362 B R + 0.027531 F + 0.004807 R


    # Adapted model 1 QoE  = 0.3*jitter*troughput/100 + 0.03*framerate + 0.02*bitrate*resolution/100 + 0.59*MOS
    # Adapted model 1 QoE  = 0.00836 TJ2+ 0.3078 TJ +  0.0060858 B F^2 R^2 + MOS  + 0.1127 B F R^2 ->  B R^2 is replaced with the MOS score

    # weights for terms for QoE calculation
    FACTOR_TJ2 = 0.00836  # adapted impact: 0.00836*5*5 = 0.21
    FACTOR_TJ = 0.3078      # adapted impact: 0.3078*5 = 1.539
    FACTOR_BF2R2 = 0.0060858  # adapted impact when replace BR2 with MOS: 0.0060858*5*5 = 0.152
    FACTOR_BFR2 = 0.1127  # adapted impact when replace BR2 with MOS: 0.1127*5 = 0.56
    FACTOR_MOS = 7.6    # equal to  adapted impact: Same as original factor since only one multiplicant

    # want also want to normalize the weights
    for k in range(5):
        # simplified model
        # npOverallScore[k] = FACTOR_JT*npJitterScaled[k]*npThroughpScaled[k]/100 + FACTOR_FPS*npFpsScaled[k] + FACTOR_BR*npCodecbitScaled[k]*npPixelScaled[k]/100 + FACTOR_MOS*npMOSScaled[k]

        # original model
        # npOverallScore[k] = FACTOR_TJ2 * npJitterScaled[k] * npJitterScaled[k] * npThroughpScaled[k] + \
        #                     FACTOR_TJ * npJitterScaled[k] * npThroughpScaled[k] + \
        #                     FACTOR_BF2R2 * npCodecbitScaled[k] * npFpsScaled[k] * npFpsScaled[k] * npPixelScaled[k] * npPixelScaled[k] + \
        #                     FACTOR_BFR2 * npCodecbitScaled[k] * npFpsScaled[k] * npPixelScaled[k] * npPixelScaled[k] + \
        #                     25 * npMOSScaled[k]

        # adapted model
        npOverallScore[k] = FACTOR_TJ2 * npJitterScaled[k] * npJitterScaled[k] * npThroughpScaled[k] + \
                            FACTOR_TJ * npJitterScaled[k] * npThroughpScaled[k] + \
                            FACTOR_BF2R2 * npFpsScaled[k] * npFpsScaled[k] * npMOSScaled[k] + \
                            FACTOR_BFR2 * npFpsScaled[k] * npMOSScaled[k] + \
                            FACTOR_MOS * npMOSScaled[k]


    # return the resulting arrays in a dictionary
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

        "codecBitrates": npCodecBitrateMeans,

        "jitterMax": npjitterMax,

        "current": npCurrentMeans,

        "overallScore": npOverallScore,

        "dictlist": requests
    }

    return returnedDictTests