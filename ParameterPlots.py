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


def CalcParameterPlots(args):

    ########################################  30 fps tests  ########################################
    dictsBitrates = []
    listBitratesStrings = ["300", "600", "900", "1300", "1800", "2700", "4000", "4750", "6000"]

    ##### VP8 with auto720
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(format(npArrayValue.std(), ".2f")) + " " + str(
                    format(npArrayValue.std(), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                    format(np.sqrt(npArrayValueVar.mean()), ".5f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".5f")) + "  ",
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
                print(str(format(npArrayValue.mean(), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".2f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".5f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".5f")) + " " + str(
                    format(np.sqrt(npArrayValueVar.mean()), ".5f")) + "  ", end="", flush=True)
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
                print(str(format(npArrayValue.mean(), ".2f")) + " ", end="", flush=True)
        print("\n")