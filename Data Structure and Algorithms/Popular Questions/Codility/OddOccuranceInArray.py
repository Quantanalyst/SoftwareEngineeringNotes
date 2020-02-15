# OddOccurrencesInArray

# A non-empty array A consisting of N integers is given. The array contains an odd
# number of elements, and each element of the array can be paired with another
# element that has the same value, except for one element that is left unpaired.
# For example, in array A such that:
#
#  A[0] = 9  A[1] = 3  A[2] = 9
#  A[3] = 3  A[4] = 9  A[5] = 7
#  A[6] = 9
#the elements at indexes 0 and 2 have value 9,
#the elements at indexes 1 and 3 have value 3,
#the elements at indexes 4 and 6 have value 9,
#the element at index 5 has value 7 and is unpaired.

# Write a function that, given an array A consisting of N integers fulfilling
# the above conditions, returns the value of the unpaired element.

# Write an efficient algorithm for the following assumptions:

# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.

## solution with time complexity O(n^2)
def OddOccurrencesInArray(A):
    unpaired = []
    for i in range(len(A)):   #---- O(n)
        if A[i] in unpaired:  #-----O(n)
            unpaired.remove(A[i])
        else:
            unpaired = unpaired + [A[i]]
    return unpaired[0]

## solution with time complexity O(n*log n)
def solution(A):     
    if len(A) == 1:
         return A[0]
    A = sorted(A)     #---- O(n*log n)
    for i in range(0 , len (A) , 2): #---- O(n)
         if i+1 == len(A):
             return A[i]
         if A[i] != A[i+1]:
             return A[i]

## solution with time complexity O(n)
def solution(A):
   result = 0
   for number in A:
     result ^= number   #bitwise XOR
     print(result)
   return result


   
# learning notes:
#Remove all items: clear()
# e.g. A.clear()   removes the entire array
#Remove an item by index and get its value: pop()
# e.g. A.pop(0)   returns and removes the element with index 0
#Remove an item by value: remove()
# e.g. A.remove(X)   removes the element with value 'X'
#Remove items by index or slice: del
# e.g. del A[0]  removes the element with index 0
#Remove multiple items that meet the condition: List comprehensions