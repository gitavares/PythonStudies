#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:41:49 2018

@author: GiselleTavares
"""

#stuff = ["iBoy", "iGirl", "iQ", "iC", "iPaid", "iPad"]
#stuff = ("iBoy", "iGirl", "iQ", "iC", "iPaid", "iPad")
#stuff = [("iBoy", "iGirl", "iQ", "iC", "iPaid", "iPad")]
#stuff = (["iBoy", "iGirl", "iQ", "iC", "iPaid", "iPad"], )
#stuff = ["iQ"]
#stuff = "iQ"
#
#for thing in stuff:
#    if thing == 'iQ':
#        print("Found it")

import math

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(-4))
print(math.sqrt(-4))
