"""
nodes have data and a set of adjacents
graphs have a set of nodes (not all of which are necessarily adjacent)
"""


class Node:
    def __init__(self, data=None, adjacents=None):
        self.data = data
        self.adjacents = adjacents if adjacents else set()

    def add_reciprocal_adjacency(self, node):
        self.adjacents.add(node)
        node.adjacents.add(self)


class Graph:
    def __init__(
        self, nodes=None
    ):  # sort of irrelevant, since nodes hold their own adjacency
        self.nodes = nodes if nodes else set()

    def add_all_adjacents(self):
        """Given current nodes, add all of those nodes' adjacents as nodes belonging to this graph"""
        to_visit = self.nodes
        seen = self.nodes
        while to_visit:
            current = to_visit.pop()
            self.nodes = self.nodes.union(current.adjacents)
            to_visit = to_visit.union(current.adjacents.difference(seen))
            seen = seen.union(current.adjacents)

    def traverse(self, starting_node=None):
        """Given a starting node, print all connected nodes"""
        if not starting_node:
            starting_node = (
                self.nodes.pop()
            )  # if no starting node provided, grab one at random
        to_visit = set([starting_node])
        seen = set([starting_node])
        print("Starting traversal from", starting_node.data)
        while to_visit:
            current = to_visit.pop()
            print(current.data)
            to_add = current.adjacents.difference(seen)  # adjacents - seen
            to_visit = to_visit.union(to_add)
            seen = seen.union(current.adjacents)  # lazy adding; set ignores duplicates
        print("Traversal complete")

    # def search(self, starting_node, )


if __name__ == "__main__":
    # Creating tree sample data
    # See: https://watchplayread.com/files/2015/12/Ticket-to-Ride-iOS.jpg

    montreal = Node("Montreal")
    boston = Node("Boston")
    new_york = Node("New York")
    toronto = Node("Toronto")
    sault_st_marie = Node("Sault St. Marie")
    chicago = Node("Chicago")
    pittsburgh = Node("Pittsburgh")
    washington = Node("Washington")
    montreal.add_reciprocal_adjacency(boston)
    montreal.add_reciprocal_adjacency(toronto)
    montreal.add_reciprocal_adjacency(sault_st_marie)
    boston.add_reciprocal_adjacency(new_york)
    new_york.add_reciprocal_adjacency(pittsburgh)
    new_york.add_reciprocal_adjacency(washington)
    pittsburgh.add_reciprocal_adjacency(washington)
    pittsburgh.add_reciprocal_adjacency(chicago)
    toronto.add_reciprocal_adjacency(sault_st_marie)
    toronto.add_reciprocal_adjacency(chicago)

    atlanta = Node("Atlanta")
    nashville = Node("Nashville")
    raleigh = Node("Raleigh")
    little_rock = Node("Little Rock")
    atlanta.add_reciprocal_adjacency(nashville)
    atlanta.add_reciprocal_adjacency(raleigh)
    nashville.add_reciprocal_adjacency(raleigh)
    nashville.add_reciprocal_adjacency(little_rock)

    ticket_to_ride = Graph(set([montreal, atlanta]))
    ticket_to_ride.traverse(atlanta)
    ticket_to_ride.traverse(new_york)
    print("Nodes:")
    print(len(ticket_to_ride.nodes))
    print("add all nodes' adjacents")
    ticket_to_ride.add_all_adjacents()
    print("Nodes:")
    print(len(ticket_to_ride.nodes))
