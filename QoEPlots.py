
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

from combinedParser import analyzeTestCustom


def Calc2Dand3Dplots(args):
    # ################### H264 30 fps
    # dictsBitratesSmall = []
    # dictsBitratesLarge = []
    # dictsBitratesAuto720 = []
    # dictsBitratesAuto = []
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

    # ################### VP8 30 fps
    # dictsBitratesSmall = []
    # dictsBitratesLarge = []
    # dictsBitratesAuto720 = []
    # dictsBitratesAuto = []
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="300",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="600",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="900",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesSmall.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
    #                                        res1="_small_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    #
    #
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="300",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="600",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="900",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
    # #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesLarge.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
    #                                        res1="_large_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    #
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="300",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="600",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="900",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
    #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
    # #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # # dictsBitratesAuto720.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
    # #                                        res1="_auto720_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    #
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="300",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="600",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="900",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1300",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="1800",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="2700",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4000",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="4750",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))
    # dictsBitratesAuto.append(analyzeTestCustom(args.folderpath, bitrate1="6000",
    #                                        res1="_auto_", fps1="30", codec1="VP8", nSamplesFromTheBackN=60))


    ###### VP8 resolution limited vs also bitrate
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

    #####################  BITRATE UNLIMITED ##################
    #loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # print("\n")
    # for i in range(len(dictsBitratesSmall)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayOverall = dictsBitratesSmall[i]["overallScore"][j]
    #         npArrayCurrent = dictsBitratesSmall[i]["current"][j]
    #         npArrayCheck = dictsBitratesSmall[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    # print("\n")
    #
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesLarge)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayOverall = dictsBitratesLarge[i]["overallScore"][j]
    #         npArrayCurrent = dictsBitratesLarge[i]["current"][j]
    #         npArrayCheck = dictsBitratesLarge[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    # print("\n")
    #
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesAuto720)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayOverall = dictsBitratesAuto720[i]["overallScore"][j]
    #         npArrayCurrent = dictsBitratesAuto720[i]["current"][j]
    #         npArrayCheck = dictsBitratesAuto720[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    # print("\n")
    #
    # # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    # for i in range(len(dictsBitratesAuto)):
    #     # for every bitrate we want to get the average jitter, MOS and power
    #     # loop over the requested tests within a bitrate (lines in output text)
    #     for j in range(5):
    #         npArrayOverall = dictsBitratesAuto[i]["overallScore"][j]
    #         npArrayCurrent = dictsBitratesAuto[i]["current"][j]
    #         npArrayCheck = dictsBitratesAuto[i]["dictlist"][j]["res"]
    #         # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
    #         if npArrayCheck != "null":
    #             print(str(format(npArrayOverall, ".2f")) + " " + str(format(npArrayCurrent.mean(), ".2f")) + "  ", end="", flush=True)
    # print("\n")
























    ###### H264 resolution limited vs also bitrate
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