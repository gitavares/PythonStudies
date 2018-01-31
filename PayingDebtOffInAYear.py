#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:18:07 2018

@author: GiselleTavares
"""
#problem 1
def CreditCardBalance(balance, annualInterestRate, monthlyPaymentRate):
    remainingBalance = balance
    minimumMonthlyPayment = 0.0
    monthlyInterestRate = annualInterestRate / 12
    
    for x in range(0, 12):
        minimumMonthlyPayment = monthlyPaymentRate * remainingBalance 
        monthlyUnpaidBalance = remainingBalance - minimumMonthlyPayment
        remainingBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        print(round(remainingBalance,2))
    return round(remainingBalance,2)
    
print("Remaining balance: " + str(CreditCardBalance(42, 0.2, 0.04)))


#problem 2
def MinimumFixedMonthlyPayment(balance, annualInterestRate):
    remainingBalance = balance
    monthlyInterestRate = annualInterestRate / 12
    MinFixedMonthlyPayment = 10
    
    while(remainingBalance > 0.0):
        for x in range(0, 12):
            monthlyUnpaidBalance = remainingBalance - MinFixedMonthlyPayment
            remainingBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
        if(remainingBalance > 0.0):
            MinFixedMonthlyPayment += 10
            remainingBalance = balance
        else:
            lowestPayment = MinFixedMonthlyPayment
            break
        
    return round(lowestPayment, 2)
    
print("Lowest Payment: " + str(MinimumFixedMonthlyPayment(3926, 0.2)))

#problem 3
def MinimumFixedMonthlyPaymentBisection(balance, annualInterestRate):
    def f(x):
        return pow(x,3) - x - 2 
    
    remainingBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = (balance * pow(1.0 + monthlyInterestRate,12))/12.0
    TOL = 0.01
    
    smallestMonthlyPayment = round(monthlyPaymentLowerBound, 2)
    
    while f(smallestMonthlyPayment) == 0 or (monthlyPaymentUpperBound - monthlyPaymentLowerBound)/2.0 > TOL:
        for x in range(0, 12):
            monthlyUnpaidBalance = remainingBalance - smallestMonthlyPayment
            remainingBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),3)
        #print('remainingBalance=', remainingBalance, 'smallestMonthlyPayment=', smallestMonthlyPayment)
        
        if(remainingBalance <= 0):
            monthlyPaymentUpperBound = round(smallestMonthlyPayment,2)
        else:
            monthlyPaymentLowerBound = round(smallestMonthlyPayment,2)

        smallestMonthlyPayment = round((monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2.0, 2)
        remainingBalance = balance
    return round(smallestMonthlyPayment, 2)    
print("Lowest Payment: " + str(MinimumFixedMonthlyPaymentBisection(320000, 0.2)))    




#problem 3
#def MinimumFixedMonthlyPaymentBisection(balance, annualInterestRate):
#    def f(x):
#        return pow(x,2) - x - 1 
#    
#    monthlyInterestRate = annualInterestRate / 12.0
#    monthlyPaymentLowerBound = balance / 12
#    monthlyPaymentUpperBound = (balance * pow(1.0 + monthlyInterestRate,12))/12.0
#    TOL = 1
#    
#    smallestMonthlyPayment = round((monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2.0, 2)
#    while f(smallestMonthlyPayment) == 0 or (monthlyPaymentUpperBound - monthlyPaymentLowerBound)/2.0 > TOL:
#        print(smallestMonthlyPayment)
#        if(f(smallestMonthlyPayment) == 0):
#            break
#        elif((f(smallestMonthlyPayment) * f(monthlyPaymentLowerBound)) < 0):
#            monthlyPaymentUpperBound = round(smallestMonthlyPayment,2)
#            smallestMonthlyPayment = round((smallestMonthlyPayment + monthlyPaymentLowerBound)/2.0, 2)
#        else:
#            monthlyPaymentLowerBound = round(smallestMonthlyPayment,2)
#            smallestMonthlyPayment = round((smallestMonthlyPayment + monthlyPaymentUpperBound)/2.0, 2) 
#        
#    return round(smallestMonthlyPayment, 2)    
#print("Lowest Payment: " + str(MinimumFixedMonthlyPaymentBisection(320000, 0.2)))    





#Hi Mandi,
#
#It's best not to post more than a couple lines or so, on a PSET. I added the following line, after I calculated what the ending balance was after each 12-month period:
#
#print("bal =", round(new_balance, 3), "payment =", round(pay_amt, 2))
#
#The results I got for each calculation on Test Case 1 were as follows. (Using an epsilon of > one cent.)
#
#bal = 33328.982 payment = 26666.67
#bal = -5818.742 payment = 29591.88
#bal = 13755.12 payment = 28129.27
#bal = 3968.189 payment = 28860.58
#bal = -925.277 payment = 29226.23
#bal = 1521.456 payment = 29043.4
#bal = 298.09 payment = 29134.82
#bal = -313.593 payment = 29180.52
#bal = -7.752 payment = 29157.67
#bal = 145.169 payment = 29146.24
#bal = 68.709 payment = 29151.96
#bal = 30.478 payment = 29154.81
#bal = 11.363 payment = 29156.24
#bal = 1.806 payment = 29156.96
#bal = -2.973 payment = 29157.31
#bal = -0.584 payment = 29157.13
#bal = 0.611 payment = 29157.04
#bal = 0.014 payment = 29157.09
#bal = -0.285 payment = 29157.11
#bal = -0.136 payment = 29157.1
#bal = -0.061 payment = 29157.09
#bal = -0.024 payment = 29157.09
#bal = -0.005 payment = 29157.09
#
#Lowest Payment: 29157.09













