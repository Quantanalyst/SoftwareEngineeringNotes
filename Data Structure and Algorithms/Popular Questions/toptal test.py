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
    else:
        uniquecolor = A[0][0]
        arr.remove(0)
        for i in range(1, M*N):
            if i in arr:
                row = i//M
                col = i % M
                if A[row][col] != uniquecolor:
                    numcountries +=1
                    uniquecolor = A[row][col]
                    arr.remove(i)
                    
            else:
                pass
    




A = [[2,3,4],[6,3,8],[9,5,1]]














