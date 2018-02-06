#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:06:34 2018

@author: GiselleTavares
"""

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1.join(s1[0:len(s1)]).join(s2[0:len(s2)])
    return helpLaceStrings(s1, s2, '')

print(laceStringsRecur('giselle', 'peri'))