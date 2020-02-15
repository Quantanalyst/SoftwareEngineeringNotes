# Triangle
# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
# if 0 ≤ P < Q < R < N and:
#
#A[P] + A[Q] > A[R],
#A[Q] + A[R] > A[P],
#A[R] + A[P] > A[Q].

#For example, consider array A such that:
#
#  A[0] = 10    A[1] = 2    A[2] = 5
#  A[3] = 1     A[4] = 8    A[5] = 20
#Triplet (0, 2, 4) is triangular.

#Write a function that, given an array A consisting of N integers, returns 1 if
# there exists a triangular triplet for this array and returns 0 otherwise.

#For example, given array A such that:

#  A[0] = 10    A[1] = 2    A[2] = 5
#  A[3] = 1     A[4] = 8    A[5] = 20
#the function should return 1, as explained above. Given array A such that:

#  A[0] = 10    A[1] = 50    A[2] = 5
#  A[3] = 1
#the function should return 0.

#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [0..100,000];
#each element of array A is an integer within the range
# [−2,147,483,648..2,147,483,647].

# solution with O(n^3) time complexity
def solution(A):
    N = len(A)
    triplet = 0 
    if N < 3:
        return triplet
    for i in range(N-2): #--- O(n)
        for j in range(i+1,N-1): #--- O(n)
            for k in range(j+1,N): #--- O(n)
                cond1 = A[i] + A[j] > A[k]
                cond2 = A[k] + A[j] > A[i]
                cond3 = A[k] + A[i] > A[j]
                if cond1 & cond2 & cond3:
                    triplet = 1
    return triplet
                
A = [10,2,5,1,8,20]
solution(A)

# solution with O(n*logn) complexity
def solution(A):
    N = len(A)
    triplet = 0 
    if N < 3:
        return triplet
    A = sorted(A)
    for i in range(0,N-2):
        if A[i]+A[i+1] > A[i+2]:
            triplet = 1            
    return triplet

           
A = [10,2,5,1,8,20]
solution(A)