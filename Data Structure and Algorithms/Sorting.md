# Sorting

It refers to arranging the data in a particular format, either ascending or descending. 

Types:
  - On the basis of 'Space'
    * In-Place: doesn't require any extra space for sorting, e.g. Bubble sort
    * Out-Place: requires extra space for sorting, e.g. Merge sort
  - On the basis of 'Stability'
    * Stable: doesn't change the sequence of the similar content in which they appear, e.g. Insertion sort. The concept of Stability is very import for 'Group By' in databases. So, in those circumstances, the sorting algorithm must return a stable sorted array. 
    * Unstable: changes the sequence of the similar content, e.g. Quick sort

Terminology: 
  - Increasing order: next > previous
  - Decreasing order: next < previous
  - Non-Increasing order: next <= previous (when there is duplicate)
  - Non-Decreasing order: next >= previous (when there is duplicate)

Sorting Algo: 
  - Bubble sort
  - Selection sort
  - Insertion sort
  - Bucket sort
  - Merge sort
  - Quick sort
  - Heap sort
  - Topological sort (for graphs) 

## Bubble sort

Repeatedly steps through the list and compares each pair of adjacent items and swaps them if they are in wrong order

Time Complexity O(n^2)
Space Complexity O(1)

When to use:
  - When input is already sorted
  - When there is a space limit
  - Easy implementation
When to avoid:
  - When time is important

## Selection sort

Repeatedly steps through the unsorted array, finds the min/max element and put it in its correct position in the sorted array

Time Complexity O(n^2)
Space Complexity O(1)

When to use:
  - When input is already sorted
  - When there is a space limit
  - Easy implementation
When to avoid:
  - When time is important

## Insertion sort

The algo. divides the array into 2 parts, i.e. sorted and unsorted. Then from the unsorted picks the first element and find its correct position in a sorted way by **comparing** and **pair-wise swapping**. It repeats until unsorted array is empty. 

Time Complexity O(n^2)  --> O(n) for scanning the array, and O(n) for comparing and swapping. Even if we improve comparing operation with Binary Search to O(log n), the swapping operation is still O(n)
Space Complexity O(1)

When to use:
  - When there is a space limit
  - Easy implementation
  - Best when we have continuous inflow of numbers and we want to keep the list sorted. 
When to avoid:
  - When time is important

## Bucket sort

The algo. works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually. 

Algorithm:
  1. Create Number of Buckets = ceil/floor(square root of total # buckets)
  2. Iterate though each number and place it in appropriate bucket (appropriate bucket = ceil(value*(#buckets)/max value in array)
  3. Sort all the buckets
  4. Merge all the buckets

Time Complexity O(n*log n)
Space Complexity O(n)

When to use:
  - When input is uniformly distributed over a range
  - Biggest advantage of this sort is when we use distributed computing. 
When to avoid:
  - When space is concern


## Merge sort

This algo. is a Divide and Conquer algorithm. It divides input array in two halves, keep breaking those 2 halves recursively until they become too small to be broken further. Then each of the broken pieces are merged together to inch towards final answer. 

Time Complexity O(n*log n)
Space Complexity O(n)

When to use:
  - When you need 'stable' sort
  - When average expected time is O(n*log n) 
When to avoid:
  - When space is a concern, e.g. embedded systems

## Quick sort

This algo. is a Divide and Conquer algorithm. At each step, it finds **'Pivot'** and then makes sure that all the smaller elements are left of 'Pivot' and all bigger elements are right of the 'Pivot'. Then, it recursively finds 'Pivot' for each smaller subarrays until the entire array is sorted. Keep note that unlike Merge sort, it does not require any external space. Also, it may not be an 'stable' sort. 

Time Complexity O(n*log n)
Space Complexity O(n)

When to use:
  - When average expected time is O(n*log n) 
When to avoid:
  - When space is a concern, e.g. embedded systems
  - When stable sort is required

## Heap sort

This algo. works by first organizing the data to be sorted into a special type of binary tree called heap tree. It then removes the topmost item (the largest/smallest) and inserts it in a current array. it keep doing until binary heap tree is empty. It is best suited with array implementation and doesn't work the best with LL. The output is not 'stable'

Time Complexity O(n*log n)
Space Complexity O(1)

When to use:
  - When space is a concern 
When to avoid:
  - When we need our sort to be 'stable'


## Tree comparison

Algorithm		Time		Space		Stable\
Bubble Sort		O(n^2)		O(1)		YES\
Selection Sort		O(n^2)		O(1)		NO\
Insertion Sort		O(n^2)		O(1)		YES\
Bucket Sort		O(n*log n)	O(n)		YES\
Merge Sort		O(n*log n)	O(n)		YES\
Quick Sort		O(n*log n)	O(n)		NO\
Heap Sort		O(n*log n)	O(1)		NO\






