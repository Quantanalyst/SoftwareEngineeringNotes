#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:46:47 2020

@author: saeed
"""

def solution(N,K):
    if N < 2:
        return 0
    else: 
        if K == 0:
            return N - 1
        elif (K !=0) & ((N // (2**K)) > 0):
            X = N // (2**K)
            res = N % (2**K)
            return (X-1) + K + res -1
        else:
            for k in range(0,K):
                if (N//(2**k)) == 1:
                    idx = k
            X = N // (2**idx)
            res = N % (2**idx)
            return (X-1) + idx + res -1
                    
            
    
solution(18,2)



def solution(A): 
    numcountries = 1
    N = len(A)     # number of rows
    M = len(A[0])  # number of columns
    arr = [i for i in range(M*N)]
    if (M == 1) & (N ==1):
        return 1
#    else:
#        uniquecolor = A[0][0]
#        arr.remove(0)
#        for i in range(1, M*N):
#            if i in arr:
#                row = i//M
#                col = i % M
#                if A[row][col] != uniquecolor:
#                    numcountries +=1
#                    uniquecolor = A[row][col]
#                    arr.remove(i)
#                    
#            else:
#                pass
#    




A = [[2,3,4],[6,3,8],[9,5,1]]


## # Python3 program for finding the maximum number 
# of trailing zeros in the product of the 
# selected subset of size k. 
MAX5 = 100
  
# Function to calculate maximum zeros. 
def maximumZeros(arr, n, k): 
    global MAX5 
      
    # Initializing each value with -1 
    subset = [[-1] * (MAX5 + 5) for _ in range(k + 1)] 
  
    subset[0][0] = 0
  
    for p in arr: 
          
        pw2, pw5 = 0, 0
  
        # Calculating maximal power  
        # of 2 for arr[p]. 
        while not p % 2 : 
            pw2 += 1
            p //= 2
  
        # Calculating maximal power  
        # of 5 for arr[p]. 
        while not p % 5 : 
            pw5 += 1
            p //= 5
  
        # Calculating subset[i][j] for maximum 
        # amount of twos we can collect by 
        # checking first i numbers and taking 
        # j of them with total power of five. 
        for i in range(k-1, -1, -1): 
              
            for j in range(MAX5): 
  
                # If subset[i][j] is not calculated. 
                if subset[i][j] != -1: 
                    subset[i + 1][j + pw5] = ( 
                        max(subset[i + 1][j + pw5],  
                        (subset[i][j] + pw2))) 
  
    # Calculating maximal number of zeros. 
    # by taking minimum of 5 or 2 and then 
    # taking maximum. 
    ans = 0
    for i in range(MAX5): 
        ans = max(ans, min(i, subset[k][i])) 
  
    return ans 
  
  
# Driver function 
arr = [ 50, 4, 20 ] 
k = 2
n = len(arr) 
  
print(maximumZeros(arr, n, k)) 
  
# This code is contributed by Ansu Kumari. 














