from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

if __name__ == '__main__':
    """
    SinglyLinkedList
    """
    print(f"------------ singly linked list ------------")
    # create a new linked list
    llist = SinglyLinkedList()

    # add nodes to the linked list
    llist.insert_at_end('a')
    llist.insert_at_end('b')
    llist.insert_at_begin('c')
    llist.insert_at_end('d')
    llist.insert_at_any_index('g', 2)

    # print the linked list
    print("Node Data")
    llist.print_ll()

    # remove a nodes from the linked list
    print("\nRemove First Node")
    llist.delete_first_node()
    print("Remove Last Node")
    llist.delete_last_node()
    print("Remove Node at Index 1")
    llist.delete_by_index(1)

    # print the linked list again
    print("\nLinked list after removing a node:")
    llist.print_ll()

    print("\nUpdate node Value")
    llist.update_node('z', 0)
    llist.print_ll()

    print("\nSize of linked list :", end=" ")
    print(llist.len_ll())

    """
    DoublyLinkedList
    """
    print(f"------------ doubly linked list ------------")
    # create a new linked list
    dllist = DoublyLinkedList()
    # add nodes to the linked list
    dllist.insert_at_end('a')
    dllist.insert_at_end('b')
    dllist.insert_at_begin('c')
    dllist.insert_at_end('d')
    dllist.insert_at_any_index('g', 2)

    # print the linked list
    print("Node Data")
    dllist.print_dll()

    # remove a nodes from the linked list
    print("\nRemove First Node")
    dllist.delete_first_node()
    print("Remove Last Node")
    dllist.delete_last_node()
    print("Remove Node at Index 1")
    dllist.delete_by_index(1)

    # print the linked list again
    print("\nLinked list after removing a node:")
    dllist.print_dll()

    print("\nSize of linked list :", end=" ")
    print(dllist.get_length())
