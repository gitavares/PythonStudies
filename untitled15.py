#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:11:35 2018

@author: GiselleTavares
"""

def lessThan4(aList):
    lessThan4list = []
    counter = 0

    while counter < len(aList):
        if len(aList[counter]) <= 3:
            lessThan4list.append(aList[counter])
        counter += 1
    return lessThan4list
    
print(lessThan4(["apple", "cat", "dog", "banana"]))