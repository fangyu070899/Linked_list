from node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    """
    Insert
	1. insert at begin
	2. insert at end
	3. insert at any index
    """

    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_any_index(self, data, index):
        new_node = Node(data)

        if index == 0:
            self.insert_at_begin(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return

        current_node = self.head
        position = 0
        while current_node != None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node == None:
            print('index error.')
            return
        else:
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node

    """
	Get Length of a Linked List
	"""

    def get_length(self):
        current_node = self.head
        count = 0

        while current_node != None:
            count += 1
            current_node = current_node.next

        return count

    """
    Delete
	1. Delete First Node 
	2. Delete Last Node 
	3. Delete a Node at a given Position
    """

    def delete_first_node(self):
        delete_node = self.head

        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_last_node(self):
        delete_node = self.tail
        if self.tail == None:
            return
        elif self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def delete_by_index(self, index):
        if index == 0:
            self.delete_first_node()
            return
        if index == self.get_length():
            self.delete_last_node
            return

        position = 0
        current_node = self.head

        while current_node != None and position != index:
            current_node = current_node.next
            position += 1

        if current_node == None:
            print("index error.")
        else:
            current_node.prev.next = current_node.next
            if current_node.next != None:
                current_node.next.prev = current_node.prev

    """
	Linked List Traversal
	"""

    def print_dll(self):
        current_node = self.head
        print('traversal')
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
        print('reverse')
        current_node = self.tail
        while current_node != None:
            print(current_node.data)
            current_node = current_node.prev
