#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:00:01 2018

@author: GiselleTavares
"""

s = "irutcbqb"
count = 0

for vowel in s.lower():
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count += 1
print('Number of vowels: ' + str(count))



s = "azcbobobegghakl"
count = 0

for i in range(len(s)):
    if s[i:3+i].lower() == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))



s = "abcdgdgefghijklmndggdgopqrstuvwxyz"
longest = ''
longestAux = ''
s = s.lower()

for i in range(len(s)):
    if longestAux == '':
        longestAux = s[i]
    elif s[i-1] <= s[i]:
        longestAux += s[i]
    else:
        longestAux = s[i]
        
    if len(longestAux) > len(longest):
        longest = longestAux
        
print('Longest substring in alphabetical order is: ' + str(longest))


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 