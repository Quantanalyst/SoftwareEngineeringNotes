# Nesting
# A string S consisting of N characters is called properly nested if:
#
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if string S is
# properly nested and 0 otherwise.
#
# For example, given S = "(()(())())", the function should return 1 and given
# S = "())", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".

# solution with O(n) time complexity
def solution(S):
    N = len(S)
    stack = 0
    if N == 0:
        return 1
    for i in range(N):
        if (S[i] == '(') & (stack >= 0):
            stack += 1
        elif (S[i] == ')') & (stack >= 0):
            stack -= 1
        elif (stack < 0):
            break
    if stack == 0:
        return 1
    else:
        return 0
    
#S = "(()(())())"
S = ')('
solution(S)
            