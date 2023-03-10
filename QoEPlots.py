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

import numpy as np

from combinedParser import analyzeTestCustom


def Calc2Dand3Dplots(args):
        #################### H264 30 fps
        dictsBitratesSmall = []
        dictsBitratesLarge = []
        dictsBitratesAuto720 = []
        dictsBitratesAuto = []
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="300",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="600",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="900",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
        #                                        res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        #
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="300",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="600",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="900",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
        #                                        res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="300",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="600",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="900",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
        #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        # #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
        # #                                        res1="_auto720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="300",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="600",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="900",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
        #                                        res1="_auto_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))

        ################### VP8 30 fps
        dictsBitratesSmall = []
        dictsBitratesLarge = []
        dictsBitratesAuto720 = []
        dictsBitratesAuto = []
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="300",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="600",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="900",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
                                               res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))


        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="300",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="600",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="900",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
                                               res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))

        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="300",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="600",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="900",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
                                               res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
        #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
        #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))

        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="300",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="600",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="900",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
                                               res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))

        # #####################  BITRATE auto720 vs auto2884 ##################
        # # calculate the average difference in power and QoE between auto 2448 and auto 720
        # # eg power: we need to go point by point, then take the average and then calculate the percentage
        # # average(pwr300diff = pwr3002448 - pwr300720, pwr600diff = pwr6002448 - pwr600720, ....)
        # npQoEAuto = np.empty(7)
        # npCurrentAuto = np.empty(7)
        # npQoEAuto720p = np.empty(7)
        # npCurrentAuto720 = np.empty(7)
        #
        # valuePairs = 7
        # # iterate over all bitrates to create np arrays of the bitrate
        # for i in range(valuePairs):
        #     npQoEAuto[i] = dictsBitratesAuto[i]["overallScore"][0]
        #     npArrayCurrent = dictsBitratesAuto[i]["current"][0]
        #     npCurrentAuto[i] = npArrayCurrent.mean()
        #
        #     npQoEAuto720p[i] = dictsBitratesAuto720[i]["overallScore"][0]
        #     npArrayCurrent720p = dictsBitratesAuto720[i]["current"][0]
        #     npCurrentAuto720[i] = npArrayCurrent720p.mean()
        #
        # # increase = (Final Value ??? Starting Value)/Starting value
        # IncCurrent = (npCurrentAuto - npCurrentAuto720)/npCurrentAuto720
        # IncQoE = (npQoEAuto - npQoEAuto720p) / npQoEAuto720p
        #
        # print("increase in current " + str(format(IncCurrent.mean()*100, ".2f")) + " percent")
        # print("increase in QoE " + str(format(IncQoE.mean()*100, ".2f")) + " percent")


        #####################  BITRATE auto720 vs best manual VP8 ##################
        npQoEMan = np.empty(5)
        npCurrentMan = np.empty(5)
        npQoEAuto720p = np.empty(5)
        npCurrentAuto720 = np.empty(5)
        #####################  VP8 ##################
        npQoEMan[0] = dictsBitratesLarge[0]["overallScore"][0]
        npArrayCurrent = dictsBitratesLarge[0]["current"][0]
        npCurrentMan[0] = npArrayCurrent.mean()
        npQoEAuto720p[0] = dictsBitratesAuto720[0]["overallScore"][0]
        npArrayCurrent720p = dictsBitratesAuto720[0]["current"][0]
        npCurrentAuto720[0] = npArrayCurrent720p.mean()

        npQoEMan[1] = dictsBitratesSmall[1]["overallScore"][0]
        npArrayCurrent = dictsBitratesSmall[1]["current"][0]
        npCurrentMan[1] = npArrayCurrent.mean()
        npQoEAuto720p[1] = dictsBitratesAuto720[1]["overallScore"][0]
        npArrayCurrent720p = dictsBitratesAuto720[1]["current"][0]
        npCurrentAuto720[1] = npArrayCurrent720p.mean()

        npQoEMan[2] = dictsBitratesLarge[2]["overallScore"][0]
        npArrayCurrent = dictsBitratesLarge[2]["current"][0]
        npCurrentMan[2] = npArrayCurrent.mean()
        npQoEAuto720p[2] = dictsBitratesAuto720[2]["overallScore"][0]
        npArrayCurrent720p = dictsBitratesAuto720[2]["current"][0]
        npCurrentAuto720[2] = npArrayCurrent720p.mean()

        npQoEMan[3] = dictsBitratesLarge[3]["overallScore"][0]
        npArrayCurrent = dictsBitratesLarge[3]["current"][0]
        npCurrentMan[3] = npArrayCurrent.mean()
        npQoEAuto720p[3] = dictsBitratesAuto720[3]["overallScore"][0]
        npArrayCurrent720p = dictsBitratesAuto720[3]["current"][0]
        npCurrentAuto720[3] = npArrayCurrent720p.mean()

        npQoEMan[4] = dictsBitratesLarge[4]["overallScore"][0]
        npArrayCurrent = dictsBitratesLarge[4]["current"][0]
        npCurrentMan[4] = npArrayCurrent.mean()
        npQoEAuto720p[4] = dictsBitratesAuto720[4]["overallScore"][0]
        npArrayCurrent720p = dictsBitratesAuto720[4]["current"][0]
        npCurrentAuto720[4] = npArrayCurrent720p.mean()

        # #####################  H264 ##################
        # npQoEMan[0] = dictsBitratesLarge[0]["overallScore"][0]
        # npArrayCurrent = dictsBitratesLarge[0]["current"][0]
        # npCurrentMan[0] = npArrayCurrent.mean()
        # npQoEAuto720p[0] = dictsBitratesAuto720[0]["overallScore"][0]
        # npArrayCurrent720p = dictsBitratesAuto720[0]["current"][0]
        # npCurrentAuto720[0] = npArrayCurrent720p.mean()
        #
        # npQoEMan[1] = dictsBitratesLarge[1]["overallScore"][0]
        # npArrayCurrent = dictsBitratesLarge[1]["current"][0]
        # npCurrentMan[1] = npArrayCurrent.mean()
        # npQoEAuto720p[1] = dictsBitratesAuto720[1]["overallScore"][0]
        # npArrayCurrent720p = dictsBitratesAuto720[1]["current"][0]
        # npCurrentAuto720[1] = npArrayCurrent720p.mean()
        #
        # npQoEMan[2] = dictsBitratesSmall[2]["overallScore"][0]
        # npArrayCurrent = dictsBitratesSmall[2]["current"][0]
        # npCurrentMan[2] = npArrayCurrent.mean()
        # npQoEAuto720p[2] = dictsBitratesAuto720[2]["overallScore"][0]
        # npArrayCurrent720p = dictsBitratesAuto720[2]["current"][0]
        # npCurrentAuto720[2] = npArrayCurrent720p.mean()
        #
        # npQoEMan[3] = dictsBitratesLarge[3]["overallScore"][0]
        # npArrayCurrent = dictsBitratesLarge[3]["current"][0]
        # npCurrentMan[3] = npArrayCurrent.mean()
        # npQoEAuto720p[3] = dictsBitratesAuto720[3]["overallScore"][0]
        # npArrayCurrent720p = dictsBitratesAuto720[3]["current"][0]
        # npCurrentAuto720[3] = npArrayCurrent720p.mean()
        #
        # npQoEMan[4] = dictsBitratesLarge[4]["overallScore"][0]
        # npArrayCurrent = dictsBitratesLarge[4]["current"][0]
        # npCurrentMan[4] = npArrayCurrent.mean()
        # npQoEAuto720p[4] = dictsBitratesAuto720[4]["overallScore"][0]
        # npArrayCurrent720p = dictsBitratesAuto720[4]["current"][0]
        # npCurrentAuto720[4] = npArrayCurrent720p.mean()


        # increase = (Final Value ??? Starting Value)/Starting value
        IncCurrent = (npCurrentAuto720-npCurrentMan)/npCurrentAuto720
        IncQoE = (npQoEAuto720p-npQoEMan) / npQoEAuto720p

        print("increase in current " + str(format(IncCurrent.mean()*100, ".2f")) + " percent")
        print("increase in QoE " + str(format(IncQoE.mean()*100, ".2f")) + " percent")







        #####################  BITRATE  ##################
        # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        print("\n")
        for i in range(len(dictsBitratesSmall)):
            # for every bitrate we want to get the average jitter, MOS and power
            # loop over the requested tests within a bitrate (lines in output text)
            for j in range(5):
                npArrayOverall = dictsBitratesSmall[i]["overallScore"][j]
                npArrayCurrent = dictsBitratesSmall[i]["current"][j]
                npArrayCheck = dictsBitratesSmall[i]["dictlist"][j]["res"]
                # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
                if npArrayCheck != "null":
                    print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        print("\n")

        # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        for i in range(len(dictsBitratesLarge)):
            # for every bitrate we want to get the average jitter, MOS and power
            # loop over the requested tests within a bitrate (lines in output text)
            for j in range(5):
                npArrayOverall = dictsBitratesLarge[i]["overallScore"][j]
                npArrayCurrent = dictsBitratesLarge[i]["current"][j]
                npArrayCheck = dictsBitratesLarge[i]["dictlist"][j]["res"]
                # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
                if npArrayCheck != "null":
                    print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        print("\n")

        # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        for i in range(len(dictsBitratesAuto720)):
            # for every bitrate we want to get the average jitter, MOS and power
            # loop over the requested tests within a bitrate (lines in output text)
            for j in range(5):
                npArrayOverall = dictsBitratesAuto720[i]["overallScore"][j]
                npArrayCurrent = dictsBitratesAuto720[i]["current"][j]
                npArrayCheck = dictsBitratesAuto720[i]["dictlist"][j]["res"]
                # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
                if npArrayCheck != "null":
                    print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        print("\n")

        # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        for i in range(len(dictsBitratesAuto)):
            # for every bitrate we want to get the average jitter, MOS and power
            # loop over the requested tests within a bitrate (lines in output text)
            for j in range(5):
                npArrayOverall = dictsBitratesAuto[i]["overallScore"][j]
                npArrayCurrent = dictsBitratesAuto[i]["current"][j]
                npArrayCheck = dictsBitratesAuto[i]["dictlist"][j]["res"]
                # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
                if npArrayCheck != "null":
                    print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        print("\n")
























        # ##### H264 resolution limited vs also bitrate
        # dictsBitratesLow = []
        # dictsBitratesMedium = []
        # dictsBitratesHigh = []
        # dictsBitratesUnlimited = []
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="300",res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="900",res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1800",res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="4750",res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="4750",res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_360_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_480_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_600_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_720_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_960_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_1080_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_1440_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))

        # ##### VP8 resolution limited vs also bitrate
        # dictsBitratesLow = []
        # dictsBitratesMedium = []
        # dictsBitratesHigh = []
        # dictsBitratesUnlimited = []
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="4750",res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesMedium.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_360_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_480_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_600_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_1080_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlimited.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_1440_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))



        # ##################### BITRATE UNLIMITED VS LIMITED ##################
        # #loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # print("\n")
        # for i in range(len(dictsBitratesLow)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesLow[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesLow[i]["current"][j]
        #         npArrayCheck = dictsBitratesLow[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesMedium)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesMedium[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesMedium[i]["current"][j]
        #         npArrayCheck = dictsBitratesMedium[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesHigh)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesHigh[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesHigh[i]["current"][j]
        #         npArrayCheck = dictsBitratesHigh[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesUnlimited)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesUnlimited[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesUnlimited[i]["current"][j]
        #         npArrayCheck = dictsBitratesUnlimited[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
















        # ################### VP8 vs H264
        # dictsBitratesVP8 = []
        # dictsBitratesH264 = []
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesVP8.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitratesH264.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # # ##################### VP8 vs H264 ##################
        # #loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # print("\n")
        # for i in range(len(dictsBitratesVP8)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesVP8[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesVP8[i]["current"][j]
        #         npArrayCheck = dictsBitratesVP8[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesH264)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesH264[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesH264[i]["current"][j]
        #         npArrayCheck = dictsBitratesH264[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")













        # ################### 15fps vs 30fps  H264
        # dictsBitrates15fps = []
        # dictsBitrates30fps = []
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates15fps.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="15", codec1="H264", nSamplesFromTheBackN=60))
        #
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        # dictsBitrates30fps.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_large_", fps1="30", codec1="H264", nSamplesFromTheBackN=60))
        #
        # ##################### VP8 vs H264 ##################
        # #loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # print("\n")
        # for i in range(len(dictsBitrates15fps)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitrates15fps[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitrates15fps[i]["current"][j]
        #         npArrayCheck = dictsBitrates15fps[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitrates30fps)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitrates30fps[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitrates30fps[i]["current"][j]
        #         npArrayCheck = dictsBitrates30fps[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")








        # ################### BIDIRECTIONAL
        dictsBitratesLow = []
        dictsBitratesHigh = []
        dictsBitratesUnlim = []


        ######## 480p
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_1300_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_1300_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_1300_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_1300_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_2700_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_2700_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_2700_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_2700_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_nolim_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_nolim_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_nolim_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC480", res1="_nolim_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))

        ######### 720p
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_1300_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_1300_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_1300_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_1300_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_2700_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_2700_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_2700_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_2700_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        #
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_nolim_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_nolim_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_nolim_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC720", res1="_nolim_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit", res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))

        # ######## 1080p
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_1300_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_1300_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_1300_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesLow.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_1300_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_2700_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_2700_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_2700_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesHigh.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_2700_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_nolim_720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_nolim_960_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_nolim_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        # dictsBitratesUnlim.append(analyzeTestCustom(args.folderpath, bitrate1="PC1080", res1="_nolim_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
        #
        #
        #
        #
        # ##################### BIDIR ##################
        # #loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # print("\n")
        # for i in range(len(dictsBitratesLow)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesLow[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesLow[i]["current"][j]
        #         npArrayCheck = dictsBitratesLow[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesHigh)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesHigh[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesHigh[i]["current"][j]
        #         npArrayCheck = dictsBitratesHigh[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")
        #
        # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
        # for i in range(len(dictsBitratesUnlim)):
        #     # for every bitrate we want to get the average jitter, MOS and power
        #     # loop over the requested tests within a bitrate (lines in output text)
        #     for j in range(5):
        #         npArrayOverall = dictsBitratesUnlim[i]["overallScore"][j]
        #         npArrayCurrent = dictsBitratesUnlim[i]["current"][j]
        #         npArrayCheck = dictsBitratesUnlim[i]["dictlist"][j]["res"]
        #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
        #         if npArrayCheck != "null":
        #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
        # print("\n")









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