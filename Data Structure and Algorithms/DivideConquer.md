# Divide and Conqueur

**Overview:**
  - It is an algorithmic design paradigm which works by recursively breaking down a problem into sub-problems of similar type, until these become simple enough to be solved directly. The solution to the sub-problems are then combined to give a solution to the original problem. 

**Common D&C problems:**
  - Binary Search
  - Merge Sort
  - Quick Sort
  - Fibonacci Series
  - Number Factors
  - House Thief
  - Edit distance
  - Zero/One Knapsack
  - Longest Common Subsequence
  - Longest Palindromic Subsequence
  - Longest Palindromic Substring
  - Min Cost to reach last cell
  - Num of path to last cell

**Number Factors**
  - Given N, count the number of ways to express N as sum of **1**, **3** and **4**

**House Thief**
  - There are N houses built in a line, each of which contains some value in it. A thief is going to steal the maximum value of these houses. However, he can't steal from 2 adjacent houses. What is the maximum stolen value? 

**Edit distance** --> convert one string to another
  - We are given strings s1 and s2
  - We need to convert s2 into s1 by: deleting, inserting, or replacing characters
  - Write a function to calculate the count of the minimum number of edit operations

**Zero/One Knapsack**
  - Similar to fractional knapsack with this difference that in this problem **fractional unit is not allowed**
  - Given the weights and profits of N items, we are asked to put these items in a knapsack which has a capacity 'C', with this restriction that we can not break the item into smaller units, i.e. fractional unit is not allwed. Challenge is to find the maximum profit from the items in the knapsack


**Longest Common Subsequence (LCS)**
  - We are given 2 strings, 's1' and 's2'
  - We need to find the length of the longest subsequence which is common in both strings
  - Subsequence: is a sequence that can be derived from another sequence by **deleting** some elements **without changing the order** of the remaining elements. 

**Longest Palindromic Subsequence (LPS)**
  - We are given 1 string, 's1'
  - We need to find the length of the longest palindrome in that string.
  - Subsequence: is a sequence that can be derived from another sequence by **deleting** some elements **without changing the order** of the remaining elements. 
  - Palindrome: is a string that reads the same backward as well as forward and can be of odd or even length

**Longest Palindromic Substring (LPS)**
  - We are given 1 string, 's1'
  - We need to find the length of the longest palindramic substring.
  - Substring: is a contiguous sequence of characters within a string

**Min Cost to reach last cell**
  - We are given a 2D matrix
  - Accessing each cell have a cost associated with it. 
  - We need to start from (0,0) cell and go to (n-1,n-1) cell
  - We can only go to right or down cell from current cell
  - **Challenge** is to do the traversal in minimum cost. 
  - Solution: We need to write a recursive function to go from the end to the beginning and find the minimum cost. 



