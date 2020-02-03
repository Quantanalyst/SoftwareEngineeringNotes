#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:36:19 2020

@author: saeed
"""

## Recursion
def foo(n):
    if n < 1:
        return
    else:
        foo(n-1)
    print('Hello World ' + str(n))
    
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)
    
Factorial(5)