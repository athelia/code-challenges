"""
nodes have data and a next node
linked lists have a head and possibly a tail
"""

class Node:
    def __init__(self, data=None, node=None) -> None:
        self.data = data
        self.next = node
    
    def add_next(self, node):
        self.next = node

class LinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        print('Data', data, 'not found')

    def remove_node(self, data):
        current = self.head
        while current:
            if current.next.data == data:
                current.next = current.next.next
                print('Removed node with data', data)
                return
            current = current.next
        print('Node with data', data, 'not found')
    
    def append_node(self, data):
        new = Node(data)
        current_end = self.tail
        current_end.next = new
        self.tail = new
    
    def insert_node(self, data, after_data):
        before = self.search(after_data)
        after = before.next
        new = Node(data)
        before.next = new
        new.next = after

if __name__ == '__main__':
    a = Node('apple')
    b = Node('berry')
    c = Node('cherry')
    d = Node('durian')
    e = Node('elderberry')
    f = Node('fig')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    fruits = LinkedList(head=a, tail=f)
    print(' '*5, '*'*5,'Traversing...', '*'*5, ' '*5)
    fruits.traverse()
    print(' '*5, '*'*5,'Searching for durian...', '*'*5, ' '*5)
    print(fruits.search('durian'))
    print(' '*5, '*'*5,'Searching for starfruit...', '*'*5, ' '*5)
    print(fruits.search('starfruit'))
    print(' '*5, '*'*5,'Removing cherry...', '*'*5, ' '*5)
    fruits.remove_node('cherry')
    fruits.traverse()
    print(' '*5, '*'*5,'Appending grapefruit...', '*'*5, ' '*5)
    fruits.append_node('grapefruit')
    fruits.traverse()
    print(' '*5, '*'*5,'Inserting cardamom...', '*'*5, ' '*5)
    fruits.insert_node('cardamom', 'berry')
    fruits.traverse()
