#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:39:43 2018

@author: GiselleTavares
"""

def oddTuples(aTup):
    newTuple = ()
    for x in range(1, len(aTup)+1, 2):
        newTuple += aTup[x-1:x]
    return newTuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))



#x = (1, 2, (3, 'John', 4), 'Hi')
#x[0]
#x[2]
#x[-1]
#x[2][2]
#x[2][-1]
#x[-1][-1]
#x[-1][2]
#x[0:1]
#x[0:-1]
#len(x)
#2 in x
#3 in x
#x[0] = 8


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result   

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

#print(applyEachTo([inc, square, halve, abs], -3))
#print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, max, int], -3))
#[-2, error, -3]
