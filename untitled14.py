#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:39:20 2018

@author: GiselleTavares
"""
#import math

def closest_power(base, num):
    if(base > 1 and num > 0):
        exponent = 0
        
        if num < base:
            return 0
        
        while True:
            #print('Exponent: ', exponent, 'base ** exponent: ', base ** exponent)
            if base ** exponent > num:
                previousBaseExp = base ** (exponent-1)
                if num - previousBaseExp <= (base ** exponent) - num:
                    exponent -= 1
                    break
                else:
                    break
            exponent += 1
        return exponent
    
print(closest_power(10, 550.0))