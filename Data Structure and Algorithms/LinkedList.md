# Linked List

**Definition** 
  - A linked list is a **linear** data structure where each element is a **separate** object, each element (node) of a list comprises of two items - the data and a reference to the the next node. The most powerful feature of Linked List is that of it is of variable size. 

**Linked List vs. Array:**
  - Separate Object: all nodes of array are part of one entity and can't be separated, but nodes of LL can be separated, replaced or deleted. 
  - Variable Size: LL, unlike array, has a variable size and can be expanded. 
  - Random access: LL, unlike array, can't be accessed randomly. 

**LL components:**
  - Node: Contains Data & References to the next node
  - Head: Reference to the first node in the list (This value is used to access the LL)
  - Tail: Reference to the last node in the list (This value is used to add a new node to the LL) 

**LL types:**
  - Single LL: The reference of the last node is NULL
  - Circular single LL: The reference of the last node is the address of the first node. 
  - Double LL: It has two references, one pointing to the previous node, and one point to the next node. So, we can traverse forward and backward on the LL. 
  - Circular double LL

**Practical use of LL:**
  - "Alt-Tab" button: It uses circular double LL
  - Windows Photo viewer: It uses CDLL to go back and forth b/w photos




