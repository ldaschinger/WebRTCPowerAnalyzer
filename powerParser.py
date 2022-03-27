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