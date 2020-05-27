# Linked List Practice
# Implement a linked list class. You have to define a few functions that perform the desirbale action. Your LinkedList class should be able to:

# Append data to the tail of the list and prepend to the head
# Search the linked list for a value and return the node
# Remove a node
# Pop, which means to return the first node's value and delete the node from the list
# Insert data at some position in the list
# Return the size (length) of the linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
       
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        self.head = Node(value)
        self.head.next = node

    def search(self, value):
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

    def remove(self, value):
        if self.head is None:
            return None
        node = self.head
        if node.value == value:
            self.head = node.next
            del node
            return

        while node.next:
            if node.next.value == value:
                new_next = node.next.next
                rm_node = node.next
                del rm_node
                node.next = new_next
                return

            node = node.next
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        
        return node.value

    def insert(self,value,position):
        if self.head is None:
            return None
        if position == 0:
            self.prepend(value)

        length = self.size()

        if position > length-1:
            self.append(value)
        
        node = self.head
        new_node = Node(value)
        while position > 0:
            if position == 1:
                new_node.next = node.next
                node.next = new_node 
            position-=position
            
    def size(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length


            
        


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"