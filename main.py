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



import argparse
from QoEPlots import Calc2Dand3Dplots


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

    # extract information and print out in table form for latex pgfplots
    # CalcParameterPlots(args)
    Calc2Dand3Dplots(args)




