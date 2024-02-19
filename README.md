# Linked_list

Each element of a linked list is called a node, and every node has two different fields:

1. Data contains the value to be stored in the node.
2. Next contains a reference to the next node on the list.

A linked list is a collection of nodes. The first node is called the head, and it’s used as the starting point for any iteration through the list. The last node must have its next reference pointing to None to determine the end of the list. Here’s how it looks:
![image](https://hackmd.io/_uploads/SyE15de36.png)

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

## References

https://realpython.com/linked-lists-python/
https://www.geeksforgeeks.org/python-linked-list/
https://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html
https://www.geeksforgeeks.org/time-and-space-complexity-of-linked-list/
