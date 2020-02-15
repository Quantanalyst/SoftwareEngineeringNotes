# PermCheck
# A non-empty array A consisting of N integers is given.
# A permutation is a sequence containing each element from 1 to N once, and only
# once.

# For example, array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
#    A[3] = 2
# is a permutation, but array A such that:
#
#    A[0] = 4
#    A[1] = 1
#    A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function that, given an array A, returns 1 if array A is a permutation
# and 0 if it is not.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

# solution --> O(n*logn)
def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif (N == 1) & (A[0] == 1):
        return 1
    elif (N == 1) & (A[0] != 1):
        return 0
    elif N > 1:
        A = sorted(A)   # ---- O(n*log n)
        if A[0] != 1:
            return 0
        else: 
            while N > 1:    # ---- O(n)
                if A[N-1] == A[N-2] + 1:
                    N = N - 1
                else:
                    return 0
            return 1
        
# solution --> O(n)
def solution(A):
    N = len(A)
    if N == 0:
        return 0
    elif (N == 1) & (A[0] == 1):
        return 1
    elif (N == 1) & (A[0] != 1):
        return 0
    elif N > 1:
        permarray = [0]*N
#        count = 0
    for i in range(N): #--- O(n)
        if (A[i] > N):
            return 0
        elif permarray[A[i]-1] == 0:
            permarray[A[i]-1] = 1
#            count +=1
        else:
            return 0
    return 1
            
A = [4,1,3,2]
solution(A)
A = [4,1,3]
solution(A)