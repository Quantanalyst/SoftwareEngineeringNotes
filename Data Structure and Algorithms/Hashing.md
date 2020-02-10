# Hashing

Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amounts of data to be indexed using keys commonly created by formula. 

If everything goes well, it can reduce time complexity of Insertion/Deletion/Search operation to O(1). However, there are worst case scenarios (when hash functions are not good enough) that it becomes O(n). So, the hope that we can gain O(1) with the right hashing tools is our incentive to use it. 

**Terminology::**
  - Hash Function: is any function that can be used to map data of arbitrary size to data of fixed size. 
  - Key: Input data given by user
  - Hash Value
  - Hash Table: It is a data structure which implements an associative array abstract data type, a strucutre that can map keys to values
  - Collision: It occurs when 2 different keys produce the same hash value. 

**Good Hash Function:**
  - It distributes hash values uniformly across the hash table (This property allows us to avoid collision as much as possible) 
  - It uses all the input data

**Collision Resolution Techniques:**
  - Direct Chaining: implements the buckets as LL. Colliding elements are stored in these LLs. 
  - Open Addressing:
    * Linear Probing: a strategy for resolving collisions by placing the new key into the closest following empty cell
    * Quadratic Probing: operates by taking the original hash index and adding successive values of an arbitrary quadratic polynomial until an open slot is found
    * Double Hashing: Interval between probes is completed by another hash function. 

**Pros and Cons of Collision Resolution Techniques:**
  - Direct Chaining: 
    * Pro: No fear of exhausting Hash Table buckets
    * Con: Fear of big LL, which can affect the performance big time
  - Open Addressing:
    * Pro: Easy implementation
    * Con: Fear of exhausting Hash Table Buckets (if that happens, then we would create another hash table twice the size of the previous one and reassign keys on this new table.)

If input size is known then always use 'open addressing', else can use any of the two. 
If **Deletion** is very high, then we should always go for Direct Chaining, as deletion creates holes on the hash table which large number of them can affect the performance of hashing big time. 

**Hashing vs. Tree:**

Operations		Tree		Hashing(average/worst case)\
Insertion		O(log n)		O(1)/O(n)\
Deletion		O(log n)		O(1)/O(n)\
Search			O(log n)		O(1)/O(n)\

So, in case of worst case scenario, when hash functions are not good enough, Tree can do a better job than Hashing. But if we use the right function, we can reduce the time complexity of the above operations to O(1). 

**Practical Uses of Hashing:**
  - Password Verification
  - File System: File path is mapped to physical location on disk
