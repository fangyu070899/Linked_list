from linked_list import LinkedList

if __name__ == '__main__':
    # create a new linked list
    llist = LinkedList()

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
