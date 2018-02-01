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













