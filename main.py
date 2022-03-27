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

from combinedParser import analyzeTestCustom



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
    dictsBitrates = []
    listBitratesStrings = ["300", "600", "900", "1300", "1800", "2700", "4000", "4750", "6000"]

    # ##### VP8 with auto720
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8",
                                           res4="_auto720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="VP8",
                                           res2="_auto_", fps2="30", codec2="VP8",
                                           nSamplesFromTheBackN=60))



    ##### H264 with auto720
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_large_", fps2="30", codec2="H264", res3="_auto_",
    #                                        fps3="30", codec3="H264", nSamplesFromTheBackN=60))

    # WITHOUT 720P AUTO
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264",
    #                   res2="_large_", fps2="30", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))




    ########################################  15 fps tests  ########################################
    # dictsBitrates = []
    # listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    #
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                        res4="_auto720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264",
    #                                         nSamplesFromTheBackN=60))

    # without the auto WebRTC setting for 720p
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="15", codec1="H264",
    #                   res2="_large_", fps2="15", codec2="H264", res3="_auto_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))




    # VP8 tests
    # dictsBitrates = []
    # listBitratesStrings = ["900", "1800", "4000", "6000"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="VP8",
    #                                        res2="_large_", fps2="30", codec2="VP8", res3="_auto_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))


    # # VP8 vs H264 tests
    # dictsBitrates = []
    # listBitratesStrings = ["300", "600", "900", "1300", "1800", "2700", "4000", "4750", "6000"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="300", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4750", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                         nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="30", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="VP8", res3="_large_", fps3="30", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))



    # # # 15fps vs 30fps H264
    # dictsBitrates = []
    # listBitratesStrings = ["600", "900", "1300", "1800", "2700", "4000", "6000"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="600", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="900", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1300", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="1800", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="2700", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="4000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="6000", res1="_small_", fps1="15", codec1="H264",
    #                                        res2="_small_", fps2="30", codec2="H264", res3="_large_", fps3="15", codec3="H264",
    #                                        res4="_large_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))


    # PC only
    # dictsBitrates = []
    # listBitratesStrings = ["480", "720", "1080", "720H264"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_480_", fps1="10", codec1="VP8",
    #                   res2="_480_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_720_", fps1="10", codec1="VP8",
    #                   res2="_720_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_1080_", fps1="10", codec1="VP8",
    #                   res2="_1080_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_720_", fps1="10", codec1="H264",
    #                   res2="_720_", fps2="30", codec2="H264", nSamplesFromTheBackN=60))







    # Only set res and no bitrate limit
    ####### H264 only no limit
    # dictsBitrates = []
    # listBitratesStrings = ["360-720", "960-1440"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_360_", fps1="30", codec1="H264",
    #                   res2="_480_", fps2="30", codec2="H264",
    #                   res3="_600_", fps3="30", codec3="H264",
    #                   res4="_720_", fps4="30", codec4="H264", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_960_", fps1="30", codec1="H264",
    #                   res2="_1080_", fps2="30", codec2="H264",
    #                   res3="_1440_", fps3="30", codec3="H264", nSamplesFromTheBackN=60))

    ####### VP8 only no limit
    # dictsBitrates = []
    # listBitratesStrings = ["360-720", "960-1440"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_360_", fps1="30", codec1="VP8",
    #                   res2="_480_", fps2="30", codec2="VP8",
    #                   res3="_600_", fps3="30", codec3="VP8",
    #                   res4="_720_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nolimit",
    #                   res1="_960_", fps1="30", codec1="VP8",
    #                   res2="_1080_", fps2="30", codec2="VP8",
    #                   res3="_1440_", fps3="30", codec3="VP8", nSamplesFromTheBackN=60))

    ####### H264 all resolutions one after another
    # dictsBitrates = []
    # listBitratesStrings = ["360", "480", "600", "720", "960", "1080", "1440"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="300", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="600", res2="_small_", fps2="30", codec2="H264",
    #                                        bitrate3="nolimit", res3="_360_", fps3="30", codec3="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="600", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="900", res2="_small_", fps2="30", codec2="H264",
    #                                        bitrate3="nolimit", res3="_480_", fps3="30", codec3="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="900", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="1300", res2="_small_", fps2="30", codec2="H264",
    #                                        bitrate3="nolimit", res3="_600_", fps3="30", codec3="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="1300", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="1800", res2="_small_", fps2="30", codec2="H264",
    #                                        bitrate3="2700", res3="_small_", fps3="30", codec3="H264",
    #                                        bitrate4="nolimit", res4="_720_", fps4="30", codec4="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="1800", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="2700", res2="_large_", fps2="30", codec2="H264",
    #                                        bitrate3="4000", res3="_small_", fps3="30", codec3="H264",
    #                                        bitrate4="nolimit", res4="_960_", fps4="30", codec4="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="4000", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="4750", res2="_small_", fps2="30", codec2="H264",
    #                                        bitrate3="6000", res3="_small_", fps3="30", codec3="H264",
    #                                        bitrate4="nolimit", res4="_1080_", fps4="30", codec4="H264",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="4750", res1="_large_", fps1="30", codec1="H264",
    #                                        bitrate2="6000", res2="_large_", fps2="30", codec2="H264",
    #                                        bitrate3="nolimit", res3="_1440_", fps3="30", codec3="H264",
    #                                        nSamplesFromTheBackN=60))


    # ####### VP8 all resolutions one after another
    # dictsBitrates = []
    # listBitratesStrings = ["360", "480", "600", "720", "960", "1080", "1440"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="300", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="600", res2="_small_", fps2="30", codec2="VP8",
    #                                        bitrate3="nolimit", res3="_360_", fps3="30", codec3="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="600", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="900", res2="_small_", fps2="30", codec2="VP8",
    #                                        bitrate3="nolimit", res3="_480_", fps3="30", codec3="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="900", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="1300", res2="_small_", fps2="30", codec2="VP8",
    #                                        bitrate3="nolimit", res3="_600_", fps3="30", codec3="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="1300", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="1800", res2="_small_", fps2="30", codec2="VP8",
    #                                        bitrate3="2700", res3="_small_", fps3="30", codec3="VP8",
    #                                        bitrate4="nolimit", res4="_720_", fps4="30", codec4="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="1800", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="2700", res2="_large_", fps2="30", codec2="VP8",
    #                                        bitrate3="4000", res3="_small_", fps3="30", codec3="VP8",
    #                                        bitrate4="nolimit", res4="_960_", fps4="30", codec4="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="4000", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="4750", res2="_small_", fps2="30", codec2="VP8",
    #                                        bitrate3="6000", res3="_small_", fps3="30", codec3="VP8",
    #                                        bitrate4="nolimit", res4="_1080_", fps4="30", codec4="VP8",
    #                                        nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath,
    #                                        bitrate1="4750", res1="_large_", fps1="30", codec1="VP8",
    #                                        bitrate2="6000", res2="_large_", fps2="30", codec2="VP8",
    #                                        bitrate3="nolimit", res3="_1440_", fps3="30", codec3="VP8",
    #                                        nSamplesFromTheBackN=60))


    # Bidirectional
    # dictsBitrates = []
    # listBitratesStrings = ["480", "720", "960", "auto"]
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nan",
    #                   res1="_nolim_480_", fps1="30", codec1="VP8",
    #                   res2="_auto_", fps2="30", codec2="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nan",
    #                   res1="_1300_720_", fps1="30", codec1="VP8",
    #                   res2="_2700_720_", fps2="30", codec2="VP8",
    #                   res3="_nolim_720_", fps3="30", codec3="VP8",
    #                   res4="_auto_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nan",
    #                   res1="_1300_960_", fps1="30", codec1="VP8",
    #                   res2="_2700_960_", fps2="30", codec2="VP8",
    #                   res3="_nolim_960_", fps3="30", codec3="VP8",
    #                   res4="_auto_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))
    # dictsBitrates.append(analyzeTestCustom(args.folderpath, bitrate1="nan",
    #                   res1="_1300_nolim_", fps1="30", codec1="VP8",
    #                   res2="_2700_nolim_", fps2="30", codec2="VP8",
    #                   res3="_nolim_nolim_", fps3="30", codec3="VP8",
    #                   res4="_auto_", fps4="30", codec4="VP8", nSamplesFromTheBackN=60))




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

   ################ RTT
    print("RTT:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["RTT"][j]
            npArrayValueVar = dictsBitrates[i]["RTTVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue.mean(), ".5f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".5f")) + " " + str(format(np.sqrt(npArrayValueVar.mean()), ".5f")) + "  ", end="", flush=True)
        print("\n")

   ################ OVERALL SCOOORRRE
    print("OVERALL SCORE:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["overallScore"][j]
            # npArrayValueVar = dictsBitrates[i]["RTTVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue, ".2f")) + " ", end="", flush=True)
        print("\n")

    ################ codec bitrates
    print("codec bitrates:")
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
    for i in range(len(dictsBitrates)):
        # loop over the requested tests within a bitrate (lines in output text)
        print(listBitratesStrings[i] + " ", end="", flush=True)
        for j in range(5):
            npArrayValue = dictsBitrates[i]["codecBitrates"][j]
            # npArrayValueVar = dictsBitrates[i]["RTTVar"][j]
            npArrayCheck = dictsBitrates[i]["dictlist"][j]["res"]
            # every printed line will be for a certain bitrate and every average value for a certain test within that bitrate
            if npArrayCheck != "null":
                print(str(format(npArrayValue, ".2f")) + " ", end="", flush=True)
        print("\n")









    #################### 3D an 2D plot
    # dictsBitratesSmall = []
    # dictsBitratesLarge = []
    # dictsBitratesAuto720 = []
    # dictsBitratesAuto = []
    # # listBitratesStrings = ["480", "720", "1080", "720H264"]
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


    ###################### 2D plot with overall score ##################
    # loop over the dictionaries meaning loop over the bitrates (columns in output text)
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