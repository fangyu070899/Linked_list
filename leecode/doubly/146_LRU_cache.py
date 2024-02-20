class Node:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_begin(self, key, data):
        new_node = Node(key, data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

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
        return delete_node

    def print_ll(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = dict()
        self.dll = DoublyLinkedList()
        self.num = 0

    def get(self, key: int) -> int:
        node = self.hash_map.get(key)
        if node == None:
            return -1
        else:
            self.move_to_front(node)
            return node.data

    def move_to_front(self, node):
        # move to front
        if node.prev != None:
            if node.next == None:
                node.prev.next = None
                self.dll.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.prev = None
            node.next = self.dll.head
            self.dll.head.prev = node
            self.dll.head = node

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map.keys():
            node = self.hash_map[key]
            node.data = value
            self.move_to_front(node)
            return
        else:
            self.num += 1
            if self.num > self.capacity:
                self.evict()

            self.hash_map[key] = self.dll.insert_at_begin(key, value)

    def evict(self):
        node = self.dll.delete_last_node()
        self.hash_map.pop(node.key)
        self.num -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
