#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:21:25 2018

@author: GiselleTavares
"""

def uniqueValues(aDict):
    tempaDict = aDict
    listOfKeys = {}
    counter = 0
    numValues = 0
    
    #print(sorted(aDict))
    
#    while counter < len(aDict):
    for k, v in aDict.items():
        #print('aDict.values(): ', aDict.values(), 'v: ', v)
        #print(v in aDict.values())
        #print('v:', v)
        #while counter < len(aDict):
        #for v in aDict:
        print('v: ', v, 'aDict.get(k): ', aDict.get(k))
        print('v == aDict.get(k): ', v == aDict.get(k))
        if v == aDict.get(k):
            numValues += 1
            print('numValues: ', numValues)
        
        if numValues > 1:
            numValues = 0
            break
        
        listOfKeys[k] = v
#            if numValues == 1:
        #numValues = 0
            #counter += 1

            
    
    return sorted(listOfKeys)

print(uniqueValues({1: 1, 2: 1, 3: 1}))