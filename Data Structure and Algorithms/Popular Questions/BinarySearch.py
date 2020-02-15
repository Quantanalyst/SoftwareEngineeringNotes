# Binary Search 
def solution(A, value):
    if (len(A) == 1) & (A[0] == value):
        print(f'found it: {A[0]}')
        return A[0]
    elif (len(A) == 1) & (A[0] != value):
        print('Not found it')
    elif len(A) == 0:
        print('Not found it')
    elif len(A) > 1:
        mid = len(A) // 2
        print(A[mid])
        if A[mid] == value:
            print('found it: {A[mid]}')
            return A[mid]
        elif A[mid] > value:
            A = A[0:mid]
            solution(A,value)
        elif A[mid] < value:
            A = A[mid+1:]
            solution(A,value)
    





A = [1,2,3,4,5,6,7,8,9,10]
x = solution(A,8)


