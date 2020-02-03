# Recursion

Why should we learn **Recursion**?
 - It makes the code easy to write (compared to **iterative**) whenever a given problem can be broken down into **similar sub-problem**. 
 - It is heavily used in Data Structures like Tree, Graph, etc (which are bulk of interview questions) 
 - It is heavily used in techniques like "Divide and Conquer', 'Greedy', 'Dynamic Programming' 


Format: 
  * Recursive Case: Where the function recur
  * Base Case: Where the function doesn't recur (stops)

Example: 

SampleRecursion(parameter){
  if (base case is satisfied)
    return some case case value
  else
    SampleRecursion(modified parameter)
}

Examples:
  * Factorial
  * Fibonacci Series


def Factorial(n):
    if n == 0:
        return 1
    else:
        return n*Factorial(n-1)





