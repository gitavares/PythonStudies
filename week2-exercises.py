#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:09:14 2018

@author: GiselleTavares
"""

#def square(x):
#    return x * x

#print(square(2))



def evalQuadratic(a, b, c, x):
    return (a * x**2) + (b*x) + c

print(evalQuadratic(2, 3.0, 4, 5))


def a(x):
    return x + 1

print(a(a(a(6))))


def a(x, y, z):
    if x:
        return y
    else:
        return z
    
def b(q,r):
    return a(q>r, q, r)

print(3>2, a, b)


print(b(3, 2))

x = 12
def g(x):
    x =+ 1
    def h(y):
        return x + y
    return h(6)
print(g(x))


def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)


def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)


def square(x):
    return x * x

print(square(2))

def fourthPower(x):
    return (square(x)) * (square(x))
    
print(fourthPower(2))


def odd(x):
    return x % 2 != 0
    
print(odd(8))


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))


def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

print(recurPower(2, 5))


def iterPower(base, exp):
    answer = 1
    while (exp > 0):
        answer *= base
        exp -= 1
    return answer

print(iterPower(2, 4))


def gcdIter(a, b):
    answer = 1
    smaller = 0
    
    if a < b: smaller = a
    else: smaller = b
        
    while (smaller > 1):
        if(a % smaller == 0 and b % smaller == 0):
            answer = smaller
            break
        smaller -= 1
    return answer

print(gcdIter(17,12))


def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(17,12))
    

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(5))


def isIn(char, aStr):
    middleChar = aStr[(int)(len(aStr)/2)]
    if char == middleChar:
        return True
    elif char < middleChar:
        for letter in range(0, round(len(aStr)/2)):
            if char == aStr[letter]:
                return True
    elif char > middleChar:
        for letter in range(round(len(aStr)/2), len(aStr)):
            if char == aStr[letter]:
                return True
    return False 

print(isIn('h', 'abcdefg'))    


def isIn(char, aStr):
    if aStr == '' or char == '':
        return False
    elif (int)(len(aStr)/2) > 0:
        middleChar = aStr[(int)(len(aStr)/2)]
        if char == middleChar:
            return True
        elif char < middleChar:
            return isIn(char, aStr[0:(int)(len(aStr)/2)])
        elif char > middleChar:
            return isIn(char, aStr[(int)(len(aStr)/2):len(aStr)])
    elif (int)(len(aStr)/2) == 0:
        middleChar = aStr[0]
        if char == middleChar:
            return True
    return False 

print(isIn('d', 'defghij'))    
    




































