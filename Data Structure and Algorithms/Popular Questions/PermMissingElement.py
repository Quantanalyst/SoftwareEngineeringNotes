# PermMissingElement
# An array A consisting of N different integers is given. The array contains
# integers in the range [1..(N + 1)], which means that exactly one element is
# missing.

# The goal is to find that missing element.

# Write a function that, given an array A, returns the value of the missing element.

# For example, given array A such that:
#  A[0] = 2
#  A[1] = 3
#  A[2] = 1
#  A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

def solution(A):
    N = len(A)
    if N == 0:   # standard part
        return 1
    elif (N == 1) & (A[0] == 1):
        return 2
    elif (N == 1) & (A[0] == 2):
        return 1
    else:
        A = sorted(A)   #---- O(n*logn)
        if A[0] != 1:
            return 1
        elif A[N-1] != N+1:
            return N+1
        else:
            for i in range(len(A)):  # --- O(n)
                if A[i+1] != A[i] + 1:
                    return A[i+1] - 1
        

A = []           # empty array
solution(A)
A = [2,3,4,5]    # missing value is the first element 
solution(A)
A = [2,3,1,4]    # no missing value
solution(A)
A = [2,3,1,5]    # missing value is 4
solution(A)