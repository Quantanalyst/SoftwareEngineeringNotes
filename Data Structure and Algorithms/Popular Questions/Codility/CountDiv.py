# CountDiv
# Write a function:
#def solution(A, B, K)
#that, given three integers A, B and K, returns the number of integers within the
# range [A..B] that are divisible by K, i.e.:

#{ i : A ≤ i ≤ B, i mod K = 0 }

#For example, for A = 6, B = 11 and K = 2, your function should return 3, because
# there are three numbers divisible by 2 within the range [6..11], namely 6, 8
# and 10.

#Write an efficient algorithm for the following assumptions:

#A and B are integers within the range [0..2,000,000,000];
#K is an integer within the range [1..2,000,000,000];
#A ≤ B.


# O(n) linear
def solution(A,B,K):
    div = []
    for val in range(A,B+1): # O(n)
        if (val % K) == 0:
            div.append(val)
    return len(div)
        
solution(6,11,2)


## O(1)
def solution(A,B,K):
    beg = A % K
    end = B % K
    if (beg == 0) & (end == 0): 
        return int((B-A)/K + 1)
    elif (beg == 0) & (end != 0): 
        return int((B-A-end)/K + 1)
    elif (beg != 0) & (end == 0):
        return int((B-A+beg-K)/K + 1)
    elif (beg != 0) & (end != 0): 
        return int((B-end-A+beg-K)/K + 1)
        
solution(11,14,2)