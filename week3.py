#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:39:43 2018

@author: GiselleTavares
"""

def oddTuples(aTup):
    newTuple = ('')
    for x in range(0, len(aTup), 2):
        newTuple += aTup[x]
    return newTuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
        