#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:25:44 2018

@author: giselletavares
"""

import numpy
import pandas
import matplotlib
import math
import random
import statsmodels
import pandas_datareader
import numpy
import numpy as np

a = np.array([[0,1,2,3],[4,5,6,7]])

from pandas_datareader import data as wb

PG = wb,DataReader('PG', data_source = 'yahoo', start = '1995-1-1')