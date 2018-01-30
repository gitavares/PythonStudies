#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:04:07 2018

@author: GiselleTavares
"""

low = 0
high = 100
guessNumber = int((high-low)/2)
indicate = ''

print("Please think of a number between 0 and 100!")

while indicate != 'c':
    print("Is your secret number " + str(int(guessNumber)) + "? ")
    indicate = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ").lower()
    
    if indicate == 'l':
        low = int(guessNumber)     
    elif indicate == 'h':
        high = int(guessNumber)
    elif indicate == 'c':
        print("Game over. Your secret number was: " + str(int(guessNumber)))
        break;
    else:
        print("Sorry, I did not understand your input.")
    guessNumber = int(high+low)/2
    
