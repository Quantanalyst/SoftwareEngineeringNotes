# MinAvgTwoSlice
# A non-empty array A consisting of N integers is given. A pair of integers
# (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that 
# the slice contains at least two elements). The average of a slice (P, Q) is
# the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. 
# To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
# 
#
#For example, array A such that:
#
#    A[0] = 4
#    A[1] = 2
#    A[2] = 2
#    A[3] = 5
#    A[4] = 1
#    A[5] = 5
#    A[6] = 8
#contains the following example slices:

#slice (1, 2), whose average is (2 + 2) / 2 = 2;
#slice (3, 4), whose average is (5 + 1) / 2 = 3;
#slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
#The goal is to find the starting position of a slice whose average is minimal.

# Write a function that, given a non-empty array A consisting of N integers,
# returns the starting position of the slice with the minimal average. If there
# is more than one slice with a minimal average, you should return the smallest
# starting position of such a slice.
#
#For example, given array A such that:
#    A[0] = 4
#    A[1] = 2
#    A[2] = 2
#    A[3] = 5
#    A[4] = 1
#    A[5] = 5
#    A[6] = 8
#the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

def solution(A): #--- O(n^3)
    N = len(A)
    minavg = (A[0]+A[1])/2
    minelement = 0
    for i in range(N): #--- O(n)
        for j in range(i+1,N): #--- O(n)
            if sum(A[i:j+1])/(j-i+1) < minavg: #--- O(n)
                minavg = sum(A[i:j+1])/(j-i+1)
                minelement = i
    return minelement
    
    
    
A = [4,2,2,5,1,5,8]
solution(A)

## Better solution: O(n)
# The argument is simple. We must all slices of size two and three. We don't 
# need to check four and higher. Because four is composed of two slices of size
# two and an average of one of them is higher than the other. If so, then that
# slice is better than the over four slice piece. The only way that four slice
# piece might have a MA is that both of two slices have the same values and in
# that case, we must pick the first slice anyway.   
def solution(A):
    min_avg_value = (A[0] + A[1])/2.0   # The mininal average
    min_avg_pos = 0     # The begin position of the first slice with MA
    for index in range(0, len(A)-2):
        # Try the next 2-element slice
        if (A[index] + A[index+1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index+1] + A[index+2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1] + A[index+2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1]+A[-2])/2.0 < min_avg_value:
        min_avg_value = (A[-1]+A[-2])/2.0
        min_avg_pos = len(A)-2
    return min_avg_pos

A = [4,2,2,5,1,5,8]
solution(A)