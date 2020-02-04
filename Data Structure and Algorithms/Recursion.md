# Recursion

**Why should we learn Recursion?**
 - It makes the code easy to write (compared to **iterative**) whenever a given problem can be broken down into **similar sub-problem**. 
 - It is heavily used in Data Structures like Tree, Graph, etc (which are bulk of interview questions) 
 - It is heavily used in techniques like "Divide and Conquer', 'Greedy', 'Dynamic Programming' 


Recursion Format: 
  * Recursive Case: Where the function recur
  * Base Case: Where the function doesn't recur (stops)

Example: 

SampleRecursion(parameter){\
  if (base case is satisfied)\
    return some case case value\
  else\
    SampleRecursion(modified parameter)\
}

Examples:
  * Factorial
  * Fibonacci Series


def Factorial(n):\
    if n == 0:\
        return 1\
    else:\
        return n*Factorial(n-1)


**Recursion vs. Iteration:**
  - Iteration is more space efficient (as it doesn't need stack memory to keep track of each recursion)
  - Iteration is more time efficient ( as it doesn't need push/pop operation on stack memory, which takes time) 
  - Recursion is easier to code (to solve subproblems)


**When to use/avoid Recursion?**
  - When to use:
    * When we can easily break down a problem into similar subproblems
    * When we are Ok with extra overhead (both time and space) that comes with it
    * When we need a quick working solution instead of an efficient one
  - When to avoid:
    * if the response to any of the above statement is NO. 

For example, when we are working with Embedded systems, which we have space limitations, iterations is a better solution. Or, when we are developing for a mission critical problem, which even a fraction of second matters, e.g. air bag, airplane control, ... 

**Practical use of Recursion:**
  - Stack
  - Tree - traversal/searching/insertion/deletion
  - Sorting - quick sort/ merge sort
  - Divide and Conquer
  - Dynamic Programming
  - etc 





