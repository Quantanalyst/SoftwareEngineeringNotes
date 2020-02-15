# Cyclic Rotation
# An array A consisting of N integers is given. Rotation of the array means that
# each element is shifted right by one index, and the last element of the array
# is moved to the first place. For example, the rotation of array
# A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index
# and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be
# shifted to the right K times.


def CyclicRotation(arr, step):
    if len(arr) == 0:
        return arr
    if step > len(arr):
        step = step % len(arr)
    arr = arr[-step:] + arr[:-step]
    return arr
    
    
    
A = [1,2,3,4,5,6,7,8]
CyclicRotation(A,3)  # correct answer --> [6, 7, 8, 1, 2, 3, 4, 5]