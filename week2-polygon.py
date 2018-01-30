#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:50:30 2018

@author: GiselleTavares
"""
import math
def polysum(n, s):
    area = 0.25 * n * (s**2)/math.tan(math.pi/n)
    square = (s*n)**2
    return round(area + square,4)

print(polysum(31,15))

