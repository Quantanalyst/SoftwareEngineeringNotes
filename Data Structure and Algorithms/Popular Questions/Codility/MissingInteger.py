# MissingInteger
# This is a demo task.

# Write a function that, given an array A of N integers, returns the smallest
# positive integer (greater than 0) that does not occur in A.
#
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
#Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# solution with O(n*logn)
def solution(A):
    N = len(A)
    if N == 0:
        return 1
    elif (N==1) & (A[0] == 1):
        return 2
    elif (N==1) & (A[0] != 1):
        return 1
    elif N > 1:
        A = sorted(A)
        if A[N-1] <= 0: 
            return 1
        else:
            missinginteger = 1
            for i in range(N):
                if (A[i] > 0) & (A[i] == missinginteger):
                    missinginteger += 1
    return missinginteger
            

A = [1, 3, 6, 4, 1, 2]
A = [-1,-3]
solution(A)