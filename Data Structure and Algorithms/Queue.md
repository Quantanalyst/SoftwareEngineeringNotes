# Queue

**Definition:**
A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

Insert in Queue language is called "enque" and "access" is called "deque". 

**note**
For Queue implementation, the time complexity for all common operation, e.g. create, enque, deque, peek, delete) is O(1) for both array and LL implementation. However, the space complexity for creation of the Queue is O(n) for array and O(1) for LL. So, **in the case of Queue, we can say that LL implementaion is more space efficient**. 

When to use/avoid?
  - When to use:
    * Helps manage the data in particular way (FIFO)
    * Can not be easily corrupted (No one can insert data in the middle)
  - When to avoid:
    * Random access not possible - if we have done some mistake, it is costly to rectify. 

