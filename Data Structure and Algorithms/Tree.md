# Tree

A tree is a collection of nodes connected by directed (or undirected) edges. A tree is a **nonlinear** data structure, compared to arrays, linked lists, stacks and queues which are linear data structures. A tree can be empty with no nodes or a tree is a structure consisting of one node called the root and zero or one or more subtrees. A tree has following general properties:
  * One node is distinguished as a root;
  * Every node (exclude a root) is connected by a directed edge from exactly one other node; A direction is: parent -> children

Each node can have arbitrary number of children. Nodes with no children are called leaves, or external nodes.

## Binary Tree

learning Binary tree is a prerequisite for more advanced trees (BST, AVL, Red-Black, Expression tree, etc). Moreover, it is used in solving specific problem like Huffman conding, Heap (priority Queue), and Expression parsing. 


**Properties of Binary Tree**
  - Used to represent data in hierarchical form
  - Every node (ideally) has 2 components (Data & Reference) 
  - It has a Root node and 2 disjoint binary tree called Left subtree and Right subtree

**Types of Binary Tree:**
  - Strict Binary Tree: if each node has either 2 children or none. 
  - Full Binary Tree: if each non-leaf node has 2 children **&** all leaf nodes are at the same level
  - Complete Binary Tree: if all levels are completely filled except possibly the last level **&** the last level has all keys as left as possible. 

**Practical Applications**
  - file system

## Binary Search Tree

BST is a binary tree in which all the nodes follow the below properties:
  - the left-subtree of a node has a key LESS than or EQUAL to its parent node's key
  - the right-subtree of a node has key GREATER than to its parent node's key


**Why should we learn Binary Search Tree?**
In terms of space efficiency, LL is a clear winner compared to array when we don't know the data size. However, these two DS have O(n) for basic operations like insertion, deletion, search, traversing. There are situations that BST can improve the time complexity of these operations. 

## AVL Tree

Depending on incoming data, a BST can get skewed and hence its performance starts going down. Instead of O(log n) for insertion/searching/deleting it can go up to O(n). AVL tree attempts to solve this problem of "skewing" by introducing a concept called "Rotation". 


## Binary Heap 

  - Definition: Binary Heap is a Binary Tree with some special properties
  - Properties
    * Heap property
      - Min-Heap: Value of any given node must be <= value of its children
      - Max-Heap: Value of any given node must be >= value of its children
    * Complete Tree
      - All levels are completely filled except possibly the last level **&** the last level has all keys as left as possible. 
      - This makes Binary Heap ideal candidate for **Array implementation**
  - Why should we learn it?
    * There are cases when we want to find min/max number among a set of numers in O(log n) time. Also, we want to make sure that **inserting** aditional numbers does not take more than O(log n) time
    * Practical use:
      * Prim's Algorithm
      * Heap sort
      * Priority Queue
  - Notes:
    * A heap is not a sorted structure; it can be regarded as being partially ordered. 
    * A heap is a useful DS when it is necessary to repeatedly remove the object with the highest (or lowest) priority.


**NOTE:** Array implementation of Binary Heap is more efficient as the primary goal of this DS is to work with Max/Min, and extractMin/extractMax for this DS has time complexity of O(log n) for array implementation and O(n) for LL implementation. For that reason, we must avoid to implement Binary Heap by LL implementation. 

## Trie

**What is Trie?**
  - It is a search tree, which is typically use to store/search strings in space/time efficient way
  - In it, any node can store non-repetitive multiple character/s
  - Every node stores 'link' of next character of the string
  - Every node keeps a track of 'end of string'

It is used to solve many standard problems in efficient ways:
  - Spelling Checker
  - Auto Complete String







