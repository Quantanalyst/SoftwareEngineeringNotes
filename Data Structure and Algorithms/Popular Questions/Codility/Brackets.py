# Brackets
# A string S consisting of N characters is considered to be properly nested
# if any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if S is properly
# nested and 0 otherwise.

#For example, given S = "{[()()]}", the function should return 1 and given
# S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..200,000];
# string S consists only of the following characters:
# "(", "{", "[", "]", "}" and/or ")".

# incomplete attempt
def solution(S):
    N = len(S)
    bracketstack = []
    curlystack = []
    parantstack = []
    for i in range(N):
        if (S[i] == '('):
            parantstack.append(i)
        elif (S[i] == '['):
            bracketstack.append(i)
        elif (S[i] == '{'):
            curlystack.append(i)
        
        elif (S[i] == ')') & (len(parantstack) > 0):
            if (len(curlystack) == 0) & (len(bracketstack) == 0):
                parantstack.pop()
            elif (len(curlystack) != 0) & (len(bracketstack) == 0) & (parantstack[-1] > curlystack[-1]):
                parantstack.pop()
            elif (len(curlystack) == 0) & (len(bracketstack) != 0) & (parantstack[-1] > bracketstack[-1]):
                parantstack.pop()
            elif (len(curlystack) != 0) & (len(bracketstack) != 0) & (parantstack[-1] > bracketstack[-1]) & (parantstack[-1] > curlystack[-1]):
                parantstack.pop()
        
        elif (S[i] == ']') & (len(bracketstack) > 0):
            if (len(curlystack) == 0) & (len(parantstack) == 0):
                bracketstack.pop()
            elif (len(parantstack) == 0) & (bracketstack[-1] > curlystack[-1]):
                bracketstack.pop()
            elif (len(curlystack) == 0) & (len(parantstack) != 0) & (bracketstack[-1] > parantstack[-1]):
                bracketstack.pop()
            elif (len(curlystack) != 0) & (len(parantstack) != 0) & (bracketstack[-1] > curlystack[-1]) & (bracketstack[-1] > parantstack[-1]):
                bracketstack.pop()
            
        elif (S[i] == '}') & (len(curlystack) > 0):
            if (len(bracketstack) == 0) & (len(parantstack) == 0):
                curlystack.pop()
            elif (len(bracketstack) != 0) & (len(parantstack) == 0) & (curlystack[-1] > bracketstack[-1]):
                curlystack.pop()
            elif (len(bracketstack) == 0) & (len(parantstack) != 0) & (curlystack[-1] > parantstack[-1]):
                curlystack.pop()
            elif (len(bracketstack) != 0) & (len(parantstack) != 0) & (curlystack[-1] > bracketstack[-1]) & (curlystack[-1] > parantstack[-1]):
                curlystack.pop()
            
        else:
            break
    if (len(parantstack) == 0) & (len(curlystack) == 0) & (len(bracketstack) == 0):
        return 1
    else:
        return 0
    
S = "{[()()]}"
solution(S)
S = "([)()]"
solution(S)
S = ')('
solution(S)

# solution with O(n) time complexity
def solution(S):
    if len(S) % 2 == 1:
        return 0
    matched = {"]":"[", "}":"{", ")":"("} # dictionary
    to_push = ["[", "{", "("]
    stack = []
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
    
S = "{[()()]}"
solution(S)
S = "([)()]"
solution(S)
S = ')('
solution(S)
