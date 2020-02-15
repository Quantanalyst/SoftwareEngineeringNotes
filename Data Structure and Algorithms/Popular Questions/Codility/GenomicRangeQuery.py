# GenomicRangeQuery
# A DNA sequence can be represented as a string consisting of the letters
# A, C, G and T, which correspond to the types of successive nucleotides
# in the sequence. Each nucleotide has an impact factor, which is an integer.
# Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4,
# respectively. You are going to answer several queries of the form: What is the
# minimal impact factor of nucleotides contained in a particular part of the given
# DNA sequence?

# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting
# of N characters. There are M queries, which are given in non-empty arrays P
# and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you
# to find the minimal impact factor of nucleotides contained in the DNA sequence
# between positions P[K] and Q[K] (inclusive).

# For example, consider string S = CAGCCTA and arrays P, Q such that:

#    P[0] = 2    Q[0] = 4
#    P[1] = 5    Q[1] = 5
#    P[2] = 0    Q[2] = 6
# The answers to these M = 3 queries are as follows:
#
# The part of the DNA between positions 2 and 4 contains nucleotides G and C
# (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
# The part between positions 5 and 5 contains a single nucleotide T, whose impact
# factor is 4, so the answer is 4.
# The part between positions 0 and 6 (the whole string) contains all nucleotides,
# in particular nucleotide A whose impact factor is 1, so the answer is 1.

# Write a function:

# def solution(S, P, Q)

# that, given a non-empty string S consisting of N characters and two non-empty
# arrays P and Q consisting of M integers, returns an array consisting of M
# integers specifying the consecutive answers to all queries.

# Result array should be returned as an array of integers.

# For example, given the string S = CAGCCTA and arrays P, Q such that:

#    P[0] = 2    Q[0] = 4
#    P[1] = 5    Q[1] = 5
#    P[2] = 0    Q[2] = 6
# the function should return the values [2, 4, 1], as explained above.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# M is an integer within the range [1..50,000];
# each element of arrays P, Q is an integer within the range [0..N − 1];
# P[K] ≤ Q[K], where 0 ≤ K < M;
# string S consists only of upper-case English letters A, C, G, T.

# solution with O(M*logM) complexity
def solution(S,P,Q):
    N = len(S)
    M = len(P)
    res = []
    for i in range(M):  #--- O(M)
        target = S[P[i]:Q[i]+1]
        target = sorted(target)[0] #--- O(MlogM)
        if target  == 'A':
            minimal = 1
        elif target  == 'C':
            minimal = 2
        elif target  == 'G':
            minimal = 3
        elif target  == 'T':
            minimal = 4
        res.append(minimal)
    return res

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
solution(S,P,Q)
    


# solution with O(N * M) complexity
def solution(S,P,Q):
    N = len(S)
    M = len(P)
    res = []
    for i in range(M):  #--- O(M)
        target = S[P[i]:Q[i]+1]
        target = [char for char in target]
        if 'A' in target:
                minimal = 1
                print(minimal)
        elif 'C' in target:
            minimal = 2
            print(minimal)
        elif 'G' in target:
            minimal = 3
            print(minimal)
        else:
            minimal = 4
        res.append(minimal)
    return res

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
solution(S,P,Q)


# solution with O(N * M) complexity
def solution(S,P,Q):
    N = len(S)
    M = len(P)
    res = []
    for i in range(M):  #--- O(M)
        target = S[P[i]:Q[i]+1]
        minimal = 4
        for j in range(len(target)): #--- O(N)
            if (target[j] == 'A') & (minimal > 1):
                minimal = 1
                break
            elif (target[j]  == 'C') & (minimal > 2):
                minimal = 2
            elif (target[j]  == 'G') & (minimal > 3):
                minimal = 3
        res.append(minimal)
    return res

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
solution(S,P,Q)


# solution with O(N * M) complexity
def solution(S,P,Q):
    N = len(S)
    M = len(P)
    res = []
    for i in range(M):  #--- O(M)
        target = S[P[i]:Q[i]+1]
        minimal = target[0]
        for j in range(1,len(target)): #--- O(N)
            if target[j] < minimal:
                minimal = target[j]
        if minimal == 'A':
            mm = 1
        elif minimal == 'C':
            mm = 2
        elif minimal == 'G':
            mm = 3
        elif minimal == 'T':
            mm = 4            
        res.append(mm)
    return res

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
solution(S,P,Q)


# Solution with O(N+M) --> ????
def solution(S, P, Q):
    result = []
    DNA_len = len(S)
    mapping = {"A":1, "C":2, "G":3, "T":4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
    return result


S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
solution(S,P,Q)