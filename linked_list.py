
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    """
	Insert
	1. insert at begin
	2. insert at end
	3. insert at any index
	"""

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_any_index(self, data, index):
        new_node = Node(data)
        if index == 0 and self.head == None:
            self.head = new_node
            return

        position = 0
        current_node = self.head
        while current_node != None and position+1 != index:
            current_node = current_node.next
            position += 1

        if current_node == None:
            print("index out of range")
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    """
	Update
	update the value of a node at a given position
	"""

    def update_node(self, data, index):
        position = 0
        current_node = self.head
        while current_node != None and position != index:
            current_node = current_node.next
            position += 1

        if current_node == None:
            print("index not found")
        else:
            # position == index
            current_node.data = data

    """
	Delete
	1. Delete First Node 
	2. Delete Last Node 
	3. Delete a Node at a given Position
	4. Delete a Node of a given Data
	"""

    def delete_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        prev_node = self.head

        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None

    def delete_by_index(self, index):
        position = 0
        current_node = self.head
        prev_node = self.head
        while current_node != None and position != index:
            prev_node = current_node
            current_node = current_node.next
            position += 1

        if current_node == None:
            print("index not found.")
        else:
            prev_node.next = current_node.next

    def delete_by_value(self, value):
        current_node = self.head
        prev_node = self.head

        while current_node != None:
            if current_node.data == value:
                prev_node.next = current_node.next
                current_node = prev_node
            current_node = current_node.next

    """
	Linked List Traversal
	"""

    def print_ll(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    """
	Get Length of a Linked List
	"""

    def len_ll(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count
