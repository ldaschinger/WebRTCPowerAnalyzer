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
from QoEPlots import Calc2Dand3Dplots
from ParameterPlots import CalcParameterPlots


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

    CalcParameterPlots(args)
    Calc2Dand3Dplots(args)




