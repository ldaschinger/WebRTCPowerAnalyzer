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


import pandas as pd

# simple calculation of average current from power analyzer file
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