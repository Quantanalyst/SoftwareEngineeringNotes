# FrogRiverOne
# A small frog wants to get to the other side of a river. The frog is initially
# located on one bank of the river (position 0) and wants to get to the opposite
# bank (position X+1). Leaves fall from a tree onto the surface of the river.
# You are given an array A consisting of N integers representing the falling
# leaves. A[K] represents the position where one leaf falls at time K, measured
# in seconds.
#
# The goal is to find the earliest time when the frog can jump to the other side
# of the river. The frog can cross only when leaves appear at every position
# across the river from 1 to X (that is, we want to find the earliest moment
# when all the positions from 1 to X are covered by leaves). You may assume that
# the speed of the current in the river is negligibly small, i.e. the leaves do
# not change their positions once they fall in the river.

#For example, you are given integer X = 5 and array A such that:
#
#  A[0] = 1
#  A[1] = 3
#  A[2] = 1
#  A[3] = 4
#  A[4] = 2
#  A[5] = 3
#  A[6] = 5
#  A[7] = 4
#In second 6, a leaf falls into position 5. This is the earliest time when leaves
# appear in every position across the river.

# Write a function that, given a non-empty array A consisting of N integers and
# integer X, returns the earliest time when the frog can jump to the other side
# of the river.

#If the frog is never able to jump to the other side of the river, the function
# should return −1.

# Write an efficient algorithm for the following assumptions:
# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].

## Solution with O(n^2) time complexity
def solution(X,A):
    path = []
    earliesttime = -1
    for index,value in enumerate(A): #---- O(n)
        if (value <=X) & (value not in path): #---- O(n)
            path = path + [value]
        if len(path) == X:
            earliesttime = index
            break
    return earliesttime


## Solution with O(n^2) time complexity
def solution(X,A):
    path = []
    earliesttime = -1
    for index,value in enumerate(A): #---- O(n)
        if (value <=X) & (?): #---- O(n)
            path = path + [value]
        if len(path) == X:
            earliesttime = index
            break
    return earliesttime
       
A = [3, 1, 4, 2, 3, 5, 4]
solution(5,A)

## Solution with O(n) time complexity
def solution(X, A):
    covered_time = [-1]*X  # Record the time, each position is covered
    uncovered = X          # Record the number of uncovered position
    for index in range(0,len(A)):
        if covered_time[A[index]-1] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[A[index]-1] = index
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return index
    # Finally, some positions are not covered
    return -1

A = [3, 1, 4, 2, 4, 3, 4]
solution(5,A)
