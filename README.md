# Linked_list

Each element of a linked list is called a node, and every node has two different fields:

1. Data contains the value to be stored in the node.
2. Next contains a reference to the next node on the list.

A linked list is a collection of nodes. The first node is called the head, and it’s used as the starting point for any iteration through the list. The last node must have its next reference pointing to None to determine the end of the list. Here’s how it looks:

![image](https://github.com/fangyu070899/Linked_list/blob/main/image/LLdrawio.png)

## doubly linked list

It is easier to implement Singly Linked list or Linked list,whereas it is pretty difficult to traverse that in reverse, to overcome this we can utilise Doubly LinkedList, where every node takes an additional pointer to point the former node to the element in addition to the pointer for the next node.

A doubly linked list has more efficient iteration, particularly if you need to ever iterate in reverse and more efficient deletion of particular nodes.

## Circular Linked List

The circular linked list is a linked list where all nodes are connected to form a circle. In a circular linked list, the first node and the last node are connected to each other which forms a circle. There is no NULL at the end.

![image](https://github.com/fangyu070899/Linked_list/blob/main/image/CircularLinkeList.png)

## Complexity

| Operation                   | Time Complexity (Singly Linked List) | Time Complexity (Doubly Linked List) | Space Complexity |
| --------------------------- | ------------------------------------ | ------------------------------------ | ---------------- |
| Accessing by Index          | O(n)                                 | O(n)                                 | O(1)             |
| Insertion at Beginning      | O(1)                                 | O(1)                                 | O(1)             |
| Insertion at End            | O(n)                                 | O(1)                                 | O(1)             |
| Insertion at Given Position | O(n)                                 | O(n)                                 | O(1)             |
| Deletion at Beginning       | O(1)                                 | O(1)                                 | O(1)             |
| Deletion at End             | O(n)                                 | O(1)                                 | O(1)             |
| Deletion at Given Position  | O(n)                                 | O(n)                                 | O(1)             |
| Searching                   | O(n)                                 | O(n)                                 | O(1)             |

## Linked List vs Array

Array: Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index.

![image](https://github.com/fangyu070899/Linked_list/blob/main/image/Arrays-1.png)

Linked List: Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element.

## References

- https://realpython.com/linked-lists-python/
- https://www.geeksforgeeks.org/python-linked-list/
- https://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html
- https://www.geeksforgeeks.org/time-and-space-complexity-of-linked-list/
- https://favtutor.com/blogs/doubly-linked-list-python
- https://www.geeksforgeeks.org/circular-linked-list/?ref=lbp
