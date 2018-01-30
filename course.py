#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:34:46 2018

@author: GiselleTavares
"""

var = 'Panda'
if var == "panda":
    print("Cute!")
elif var == "Panda":
    print("Regal!")
else:
    print("Ugly...")

var = 'happy'
if len(var) > 2:
    print("hello world")

varA = 5
varB = 3
            
if type(varA) == type("Brasil") or type(varB) == type("Brasil"):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

num = 10
while num > 3:
    num -= 1
    print(num)
    
num = 2
while num <= 10:
    print(num)
    num += 2
print('Goodbye!')

print('Hello!')
num = 10
while num >= 2:
    print(num)
    num -= 2
    
end = 6    
mysum = 0
count = 1
while end >= count:
    mysum += count
    count += 1
print(mysum)    


for i in range(2, 12, 2):
    print(i)
print('Goodbye!')


mysum = 0
for i in range(5,11,2):
    mysum += i
    

    print(mysum)
    
print('Hello!')
for i in range(10, 0, -2):
    print(i) 
    

end = 6    
mysum = 0
count = 1
for i in range(1, end+1):
    mysum += count
    count += 1
print(mysum) 


x = 5
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))

num = 10
for num in range(5):
    print(num)
print(num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
        
for letter in 'hola':
    print(letter)  


count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)



myStr = '6.00x'
for char in myStr:
    print(char)
print('done')      


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))



iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        
        
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))