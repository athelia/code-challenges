# CTCI Chapter 2, Linked Lists


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        return f"<Node value={self.value}" + (
            f" next={self.next}>"
            if self.next is None
            else f" next.value={self.next.value}>"
        )


class LinkedList:
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail if tail else head
        print(f"Created LinkedList head={self.head} tail={self.tail}")

    def __repr__(self):
        return f"<LinkedList head={self.head} tail={self.tail}>"

    def traverse_and_print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, node):
        self.tail.next = node
        self.tail = node
        print(f"Appended {node}")

    def extend(self, nodelist):
        for node in nodelist:
            self.append(node)
        # TODO improvement: only reassign self.tail to the last element

    def prepend(self, node):
        node.next = self.head
        self.head = node
        print(f"Prepended {node}")

    def find(self, value):
        """Given a value, return a node matching the value if found in the linked list, or None"""
        current = self.head
        while current:
            if current.value == value:
                print(f"Successfully found node with value {value}")
                return current
            current = current.next
        print(f"No node found with value {value}")
        return None

    def delete(self, value):
        if self.head.value == value:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            print(f"Successfully deleted {value}")
            return None

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                print(f"Successfully deleted {value}")
                return None
        print(f"No node found with value {value}")
        return None

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # - CTCI 2.1 + follow up, perhaps
    #     - **Remove Dups**: Write code to remove duplicates from an unsorted linked list.
    #     - FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
    #     - Hints: #9, #40
    def remove_dupes(self):
        """Given the head of an unsorted linked list, remove duplicate nodes.

        >>> n = Node('apple')

        >>> l = LinkedList(head=Node(value='apple', nxt=Node(value='berry', nxt=n)), tail=n)
        Created LinkedList head=<Node value=apple next.value=berry> tail=<Node value=apple next=None>

        >>> l.remove_dupes()
        Deleting node value apple

        >>> l.traverse_and_print()
        apple
        berry
        """
        # if allowed a buffer: use a set to track seen values
        current = self.head
        seen = {current.value}
        while current and current.next:
            if current.next.value in seen:
                # a -> b -> c -> None
                # b -> None
                # a -> c -> None
                print(f"Deleting node value {current.next.value}")
                new_next = current.next.next
                current.next.next = None
                current.next = new_next
                # TODO: if deleted node was self.tail, move self.tail back one node
                # if current.next is None, self.tail = current
            else:
                seen.add(current.next.value)
            current = current.next

    def remove_dupes_bufferless(self):
        pass
        # for each node, search for a duplicate -> O(n^2)
        # current = self.head
        # while current:
        #     # FIXME: always starts at head, so will delete the value itself and not just dupes
        #     self.delete(current.value)

    def return_kth_to_last(self, k: int) -> Node:
        """Given a singly-linked list, return the kth to last element.
        >>> n = Node('dandelion')
        >>> l = LinkedList(Node('aster', nxt=Node(value='begonia', nxt=Node(value='chrysanthemum', nxt=n))), tail=n)
        Created LinkedList head=<Node value=aster next.value=begonia> tail=<Node value=dandelion next=None>
        >>> l.return_kth_to_last(2)
        <Node value=chrysanthemum next.value=dandelion>
        >>> l.return_kth_to_last(5)
        Traceback (most recent call last):
        ...
        IndexError: LinkedList too short; cannot return k=5th to last
        """
        slow, fast = self.head, self.head
        for _ in range(k):
            fast = fast.next
            # TODO: fixme
            if fast.next is None and _ + 1 < k:
                raise IndexError(f"LinkedList too short; cannot return k={k}th to last")
        while fast:
            slow, fast = slow.next, fast.next
        return slow


# a -> b -> c -> d -> None
# k = 2
# fast  slow    _
# a     a
# b     a       0
# c     a       1
# d     b
# None  c


if __name__ == "__main__":

    def generate_fruit_ll(length):
        fruits = [
            "",
            "berry",
            "cherry",
            "durian",
            "elderberry",
            "fig",
            "grapefruit",
            "honeydew",
            "ice apple",
            "jackfruit",
            "kiwi",
            "lemon",
            "mango",
            "nectarine",
            "orange",
            "pear",
            "quince",
            "raspberry",
            "strawberry",
            "tamarind",
            "ube",
            "vanilla",
            "watermelon",
            "yuzu",
            "zante currant",
        ]
        node = Node("apple")
        linked_fruits = LinkedList(node)
        linked_fruits.extend([Node(fruit) for fruit in fruits[1:length]])
        return linked_fruits

    n1 = Node("apple")
    n2 = Node("berry")
    n3 = Node("cherry")
    n4 = Node("durian")
    n5 = Node("apple")
    ll = LinkedList(n1)
    ll.append(n2)
    ll.append(n3)
    lgth = ll.get_length()
    print(f"length={lgth}")
    ll.traverse_and_print()
    ll.find("berry")
    ll.delete("berry")
    ll.traverse_and_print()
    ll.find("berry")
    n2.next = (
        None  # otherwise n2.next is still pointing to n3, leading to a circular ll
    )
    ll.extend([n2, n4, n5])
    ll.extend([Node(fruit) for fruit in ["elderberry", "fig", "grapefruit"]])
    print(f"ll={ll}")
    # print("\n" + "~*~*~*~    Remove duplicates    ~*~*~*~")
    # ll1 = generate_fruit_ll(8)
    # ll1.extend([Node(fruit) for fruit in ["apple", "apple", "honeydew", "grapefruit"]])
    # ll1.traverse_and_print()
    # ll.remove_dupes()
    # ll1.traverse_and_print()
    print("\n" + "~*~*~*~    Return kth to last    ~*~*~*~")
    ll2 = generate_fruit_ll(15)
    ll2.traverse_and_print()
    print(f"7th to last={ll2.return_kth_to_last(7).value}")
    print(f"12th to last={ll2.return_kth_to_last(12).value}")
