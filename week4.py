#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:32:50 2018

@author: giselletavares
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
print(rem(7,5))


def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)

print(f(0))

#def fancy_divide(numbers,index):
#    try:
#        denom = numbers[index]
#        print('denom=', denom)
#        for i in range(len(numbers)):
#            print('numbers[i]=',numbers[i])
#            numbers[i] /= denom
#        print('saiu do for')
#    except IndexError:
#        print('IndexError')
#        print("-1")
#    else:
#        print('else')
#        print("1")
#    finally:
#        print('finally')
#        print("0")

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

print(fancy_divide([0, 2, 4], 0))

print(fancy_divide([0, 2, 4], 4))

print(fancy_divide([0, 2, 4], 1))
#denom = 2
#0,0,0


def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

print(fancy_divide([0, 2, 4], 0))
# -2, 0

print(fancy_divide([0, 2, 4], 4))
# denom = 4
# 1, 0, 0

print(fancy_divide([0, 2, 4], 1))
# 1, 0


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
print(fancy_divide([0, 2, 4], 0))
# 0, -2

print(fancy_divide([0, 2, 4], 4))  
# denom = 4
# 1, 0, 0
        
print(fancy_divide([0, 2, 4], 1))
# 1, 0

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
print(fancy_divide([0, 2, 4], 0))


def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
print(fancy_divide([0, 2, 4], 0))





























