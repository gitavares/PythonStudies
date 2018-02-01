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
        


#def absToEach(testList):
#    return abs(testList)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

testList = [1, -4, 8, -9]

#def plusOneToEach(testList): 
#    return testList + 1
#print(plusOneToEach(testList))


def expTwoToEach(testList): 
    return abs(testList ** 2)

#print(applyToEach(testList, absToEach))
print(applyToEach(testList, expTwoToEach))




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

# exercise how many
animals = {'a': ['aardvark'],
 'b': ['baboon'],
 'c': ['coati'],
 'd': ['donkey', 'dog', 'dingo']}
def how_many(aDict):
    sumAnimals = 0
    for animals in aDict.keys():
        for animals in aDict[animals]:    
            sumAnimals += 1
    
    return sumAnimals
print(how_many(animals))


# exercise biggest
animals = {'a': ['aardvark'],
 'b': ['baboon'],
 'c': ['coati'],
 'd': ['donkey', 'dog', 'dingo']}
def biggest(aDict):
    biggestKey = ''
    aux = 0
    aux2 = 0
    for a in aDict.keys():
        for animal in aDict[a]:    
            aux += 1
        if aux > aux2:
            biggestKey = a
            aux2 = aux
            aux = 0    
    return biggestKey
print(biggest(animals))
    
   
