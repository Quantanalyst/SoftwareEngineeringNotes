#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:36:19 2020

@author: saeed
"""

### --------------------- Recursion ------------------------------

# Format
def foo(n):
    if n < 1:
        return
    else:
        foo(n-1)
    print('Hello World ' + str(n))

# Factorial
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)
    
# Fibonacci Series
def Fibonacci(n):
    if n < 1:
        raise ValueError('Fibonacci is only for positive values')
    elif n in [1,2]:
        return n-1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
# Finding a number in a sorted array
def FindNumber(num, array):
    if len(array) == 0:
        print('This number does not exist in the array')
    else:
        pointer = int(np.ceil(len(array)/2) -1)
        if array[pointer] == num:
            return num, pointer
        elif array[pointer] > num:
            array = array[0:pointer]
            FindNumber(num,array)
        else:
            array = array[pointer+1:]
            FindNumber(num,array)
        
test = np.array([0,1,1,2,3,5,8,13,21,34])
_, index = FindNumber(3,test)