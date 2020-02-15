# PassingCars
# A non-empty array A consisting of N integers is given. The consecutive elements 
# of array A represent consecutive cars on a road.

# Array A contains only 0s and/or 1s:

# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q),
# where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q
# is traveling to the west.

#For example, consider array A such that:

#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

#Write a function that, given a non-empty array A of N integers, returns the
# number of pairs of passing cars.
#
# The function should return −1 if the number of pairs of passing cars
# exceeds 1,000,000,000.

#Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following
# values: 0, 1.

# solution with O(n^2)
def solution(A):
    maxcount = 0
    N = len(A)
    for i in range(N):  #--- O(n)
        for j in range(i+1,N):  #--- O(n)
            if maxcount > 1000000000:
                return -1
            elif (A[i] == 0) & (A[j] != A[i]):
                maxcount += 1
    return maxcount

A = [0,1,0,1,1]
solution(A)

# solution with O(n)
def solution(A):
    N = len(A)
    localcount = 0
    globalcount = 0
    for i in range(N): #--- O(n)
        if A[N-1-i] == 1:
            localcount += 1
        elif (A[N-1-i] == 0) & (globalcount <= 1000000000):
            globalcount += localcount
        else:
            return -1
    return globalcount
        

A = [0,1,0,1,1]
solution(A)            