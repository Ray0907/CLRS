# Elementary data structures

### stacks and queues

- stack and queues are dynamic sets in which the element removed from the set by the DELETE operation.
- stack: the element deleted from the set is the one most recently inserted A.K.A **_LIFO_**
  - if we attempt to pop an empty stack, we say the stack **_underflow_**
  - if S.top exceeds n, the stack **_overflow_**
- queue: the element deleted is always the one that has been in the set for the longest time. A.K.A **_FIFO_**
  - the queue has a **_head_** and **_tail_**

### Linked list

- Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.
- **_Circular linked_** list is a linked list where all nodes are connected to form a circle. There is no NULL at the end. A circular linked list can be a singly circular linked list or doubly circular linked list.
- **_Doubly Linked List (DLL)_** contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
