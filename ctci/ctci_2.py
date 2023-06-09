# CTCI Chapter 2, Linked Lists
from typing import Any, Collection, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Any] = None) -> None:
        self.value = value
        self.next = nxt

    def __repr__(self) -> str:
        return f"<Node value={self.value}" + (
            f" next={self.next}>"
            if self.next is None
            else f" next.value={self.next.value}>"
        )


class LinkedList:
    def __init__(self, head: Node, tail: Node = None, verbose: bool = None) -> None:
        """LL data structure with constant time append and prepend."""
        self.head = head
        self.tail = tail if tail else head
        if verbose:
            print(f"Created LinkedList head={self.head} tail={self.tail}")

    def __repr__(self) -> str:
        return f"<LinkedList head={self.head} tail={self.tail}>"

    def traverse_and_print(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, node: Node, verbose: bool = False) -> None:
        self.tail.next = node
        self.tail = node
        if verbose:
            print(f"Appended {node}")

    def extend(self, nodelist: Collection[Node], verbose: bool = False) -> None:
        """Like Python List extend, append every element of an iterable containing Node elements."""
        for node in nodelist:
            if type(node) is Node:
                # TODO improvement: only reassign self.tail to the last element (don't reuse .append)
                self.append(node, verbose=verbose)
            else:
                raise TypeError(
                    f"Expected Node type but got {type(node)} for element {node}"
                )

    def prepend(self, node: Node, verbose: bool = False) -> None:
        node.next = self.head
        self.head = node
        if verbose:
            print(f"Prepended {node}")

    def find(self, value: Any) -> Optional[Node]:
        """Given a value, return a node matching the value if found in the linked list, or None"""
        current = self.head
        while current:
            if current.value == value:
                print(f"Successfully found node with value {value}")
                return current
            current = current.next
        print(f"No node found with value {value}")
        return None

    def delete(self, value: Any, verbose: bool = False) -> None:
        if self.head.value == value:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            if verbose:
                print(f"Successfully deleted {value}")
            return None

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if verbose:
                    print(f"Successfully deleted {value}")
                return None
        print(f"No node found with value {value}")
        return None

    def get_length(self) -> int:
        """Get the length of a linked list by iterating through it.
        >>> ll1 = generate_fruits_ll(10)
        >>> ll1.get_length()
        10
        >>> ll2 = generate_fruits_ll(1)
        >>> ll2.traverse_and_print()
        apple
        >>> ll2.get_length()
        1

        Returns:
            int: length of linked list
        """
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
    def remove_dupes(self) -> None:
        """Given the head of an unsorted linked list, remove duplicate nodes.

        >>> n = Node('apple')

        >>> l = LinkedList(head=Node(value='apple', nxt=Node(value='berry', nxt=n)), tail=n, verbose=True)
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

    def remove_dupes_bufferless(self) -> None:
        pass
        # for each node, search for a duplicate -> O(n^2)
        # current = self.head
        # while current:

    def return_kth_to_last(self, k: int) -> Node:
        """Given a singly-linked list, return the kth to last element.
        >>> n = Node('dandelion')
        >>> l = LinkedList(Node('aster', nxt=Node(value='begonia', nxt=Node(value='chrysanthemum', nxt=n))), tail=n, verbose=True)
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

    # 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    # before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    # to be after the elements less than x (see below). The partition element x can appear anywhere in the
    # "right partition"; it does not need to appear between the left and right partitions.
    # EXAMPLE
    # Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
    # Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    def partition(self, p: int) -> None:
        current = self.head
        while current:
            current = current.next
        return None


# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
def delete_middle_node(n: Node, verbose: bool = False) -> None:
    """ 'Delete' a middle node from a linked list by reassigning the value and .next. Does not work for tail node."""
    n.value, n.next = n.next.value, n.next.next
    if verbose:
        print(f"Deleted node")
    return None


# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
def sum_lists_same_length(linked_1: LinkedList, linked_2: LinkedList) -> LinkedList:
    """ Given linked lists that represent the digits of an integer, stored ones place at the head, return the sum.
        Assumes that both linked lists have the same number of digits.
    """
    pointer_1 = linked_1.head
    pointer_2 = linked_2.head
    carried_one = 0
    result = None
    while pointer_1 or pointer_2:
        p1_value = pointer_1.value if pointer_1 else 0
        p2_value = pointer_2.value if pointer_2 else 0
        digit_sum = p1_value + p2_value + carried_one
        digit = digit_sum % 10
        if not result:
            result = LinkedList(Node(digit))
        else:
            result.append(Node(digit))
        carried_one = 1 if digit_sum > 10 else 0
        pointer_1 = pointer_1.next if pointer_1 else None
        pointer_2 = pointer_2.next if pointer_2 else None
    return result


# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output:9 -> 1 -> 2. That is, 912.


def generate_fruits_ll(length: int = 10, verbose: bool = False) -> LinkedList:
    """Helper to create a linked list of alphabetical strings. Can only be 26 elements long.

    >>> short_ll = generate_fruits_ll(1, True)
    <LinkedList head=<Node value=apple next=None> tail=<Node value=apple next=None>>
    >>> midsize_ll = generate_fruits_ll(15, True)
    <LinkedList head=<Node value=apple next.value=berry> tail=<Node value=orange next=None>>
    >>> too_big_ll = generate_fruits_ll(100)
    Traceback (most recent call last):
    ...
    Exception: Only 26 elements are specified for this method. Please choose a length integer <= 26.

    Args:
        length (int): Desired length of generated LL, up to 26 elements long
        verbose (bool): Whether to show print output for the generated LL
    Returns:
        LinkedList: Newly generated linked list
    Raises:
        Exception: If the length is greater than 26
    """
    fruits = [
        "apple",
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
    if length > 26:
        raise Exception(
            "Only 26 elements are specified for this method. Please choose a length integer <= 26."
        )
    linked_fruits = LinkedList(Node(fruits[0]))
    linked_fruits.extend([Node(fruit) for fruit in fruits[1:length]])
    if verbose:
        print(f"<LinkedList head={linked_fruits.head} tail={linked_fruits.tail}>")
    return linked_fruits
