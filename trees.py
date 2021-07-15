"""
a tree has nodes and a root
every node in a tree has data and children
children should be a ?list? or a set (nodes must be unique though data can be repeated)
"""

class Node:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children if children else []

    def add_child(self, child):
        """Given a node to add as a child, append to current node's children."""
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root    

    def df_traverse(self):
        """Traverse (depth-first) and print all nodes"""
        to_visit = [self.root]

        print('Starting depth-first traversal')
        while to_visit:
            current = to_visit.pop()
            print(current.data)
            to_visit.extend(current.children)
        print('Ended depth-first traversal')
    
    def bf_traverse(self):
        """Traverse (breadth-first) and print all nodes"""
        to_visit = [self.root]
        
        print('Starting breadth-first traversal')
        while to_visit: 
            current = to_visit.pop(0) #better runtime if we maintain a pointer
            #pointer -> while condition changes to pointer == len(to_visit)
            print(current.data)
            to_visit.extend(current.children)
        print('Ended breadth-first traversal')

    def bf_traverse_runtime(self):
        """More efficient breadth-first traversal: doesn't change to_visit list"""
        to_visit = [self.root]
        i = 0
        
        print('Starting breadth-first traversal')
        while i < len(to_visit): 
            current = to_visit[i]
            print(current.data)
            to_visit.extend(current.children)
            i += 1
        print('Ended breadth-first traversal')
    
    def search(self, data):
        """Breadth-first search"""
        to_visit = [self.root]
        i = 0

        while i < len(to_visit):
            current = to_visit[i]
            if current.data == data:
                return current
            to_visit.extend(current.children)
            i += 1
        return 'Not found'


if __name__ == '__main__':
    # Creating tree sample data
    sandi = Node('Sandi')
    ann = Node('Ann')
    john = Node('John')
    dan = Node('Dan')
    caleb = Node('Caleb')
    vivian = Node('Vivian')
    katy = Node('Katy')
    peter = Node('Peter')
    lucia = Node('Lucia')
    olivia = Node('Olivia')
    susu = Node('Susu')
    sini = Node('Sini')
    malachi = Node('Malachi')
    jeremiah = Node('Jeremiah')
    miriam = Node('Miriam')
    gideon = Node('Gideon')
    baby = Node('baby')
    sandi.add_child(ann)
    sandi.add_child(john)
    sandi.add_child(dan)
    sandi.add_child(caleb)
    ann.add_child(vivian)
    ann.add_child(katy)
    ann.add_child(peter)
    ann.add_child(lucia)
    ann.add_child(olivia)
    dan.add_child(susu)
    dan.add_child(sini)
    caleb.add_child(malachi)
    caleb.add_child(jeremiah)
    caleb.add_child(miriam)
    caleb.add_child(gideon)
    caleb.add_child(baby)
    # create tree + traverse
    family = Tree(sandi)
    family.bf_traverse()
    family.df_traverse()
    family.bf_traverse_runtime()
    print(family.search('booplesnoot'))
    print(family.search('Miriam').data)