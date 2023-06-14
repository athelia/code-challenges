# CTCI Chapter 2, Linked Lists
from typing import Any, Collection, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Any] = None) -> None:
        self.value = value
        self.next = nxt

    def __eq__(self, other: Any) -> bool:
        """Equivalence for Nodes compares only the value stored in the Node, not whatever it may be linked to."""
        return type(other) is Node and other.value == self.value

    def __ne__(self, other: Any) -> bool:
        return not self == other

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

    def __eq__(self, other: Any) -> bool:
        """A LinkedList is equivalent to another if they have the same sequence of values."""
        if type(other) is not LinkedList:
            return False
        current = self.head
        other_current = other.head
        while current or other_current:
            if current != other_current:
                return False
            else:
                current = current.next
                other_current = other_current.next
        return True

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __repr__(self) -> str:
        return f"<LinkedList head={self.head} tail={self.tail}>"

    def __reversed__(self) -> "LinkedList":
        """Easy method using already-defined prepend."""
        current = self.head
        result = None
        while current:
            if not result:
                result = LinkedList(Node(current.value))
            else:
                result.prepend(Node(current.value))
            current = current.next
        return result

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

    def reverse(self) -> Node:
        """Implements reversal when no prepend method is defined. Returns head of the reversed list."""
        current = self.head
        new_previous = None
        while current:
            new_current = current.next
            current.next = new_previous
            new_previous = current
            current = new_current
        return new_previous

    @staticmethod
    def listify_integer(i: int, stored_forwards: bool = False) -> "LinkedList":
        """Given an integer, convert it into a LinkedList of the digits.

        Args:
            i (int): the integer to convert
            stored_forwards (bool): which digit should be at the head. If True, the ones digit will be the tail.

        Returns:
            LinkedList: the integer converted to a LinkedList

        >>> LinkedList.listify_integer(123)
        <LinkedList head=<Node value=3 next.value=2> tail=<Node value=1 next=None>>
        >>> LinkedList.listify_integer(123, True)
        <LinkedList head=<Node value=1 next.value=2> tail=<Node value=3 next=None>>
        """
        result = None
        while i > 0:
            new_node = Node(i % 10)
            i = i // 10
            if not result:
                result = LinkedList(new_node)
            elif stored_forwards:
                # If we want the head to end up as the largest digit, we must push new digits to the front
                result.prepend(new_node)
            else:
                # Otherwise new digits should come afterwards
                result.append(new_node)
        return result
        # TODO: write this recursively

    # - CTCI 2.1 + follow up, perhaps
    #     - **Remove Dups**: Write code to remove duplicates from an unsorted linked list.
    #     - FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
    #     - Hints: #9, #40
    # noinspection PyUnresolvedReferences
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
        >>> l = LinkedList(Node('aster', nxt=Node(value='begonia', nxt=Node(value='chrysanthemum', nxt=n))), tail=n,\
        verbose=True)
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
    """'Delete' a middle node from a linked list by reassigning the value and .next. Does not work for tail node."""
    n.value, n.next = n.next.value, n.next.next
    if verbose:
        print(f"Deleted node")
    return None


# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
def sum_lists_ones_digit_at_head(
    linked_1: LinkedList, linked_2: LinkedList, returned_forwards: bool = False
) -> LinkedList:
    """Given linked lists that represent the digits of a positive integer with the ones place at the head,
    return the sum.

    Args:
        linked_1 (LinkedList): first integer to be added, e.g. the integer 617 becomes 7 -> 1 -> 6
        linked_2 (LinkedList): second integer to be added, e.g. the integer 295 becomes 5 -> 9 -> 2
        returned_forwards (bool): whether to return the digits of the result in forward or backward order. If True,
          the result 42 will be returned as 4 -> 2 instead of 2 -> 4.

    Returns:
        LinkedList: sum of the two integers with each digit as an individual Node.

    Raises:
        ValueError: if the value of a Node in either LinkedList is not an integer

    >>> l1, l2 = LinkedList.listify_integer(617), LinkedList.listify_integer(295)
    >>> sum_lists_ones_digit_at_head(l1, l2)
    <LinkedList head=<Node value=2 next.value=1> tail=<Node value=9 next=None>>
    >>> sum_lists_ones_digit_at_head(l1, l2, True)
    <LinkedList head=<Node value=9 next.value=1> tail=<Node value=2 next=None>>
    """
    pointer_1 = linked_1.head
    pointer_2 = linked_2.head
    carried_one = 0
    result = None
    while pointer_1 or pointer_2:
        p1_value = pointer_1.value if pointer_1 else 0
        p2_value = pointer_2.value if pointer_2 else 0
        if type(p1_value) is not int:
            try:
                p1_value = int(p1_value)
            except ValueError:
                raise ValueError(f"{p1_value} must be an integer")
        elif type(p2_value) is not int:
            try:
                p2_value = int(p2_value)
            except ValueError:
                raise ValueError(f"{p2_value} must be an integer")
        digit_sum = p1_value + p2_value + carried_one
        digit = digit_sum % 10
        if not result:
            result = LinkedList(Node(digit))
        else:
            if returned_forwards:
                result.prepend(Node(digit))
            else:
                result.append(Node(digit))
        carried_one = 1 if digit_sum > 9 else 0
        pointer_1 = pointer_1.next if pointer_1 else None
        pointer_2 = pointer_2.next if pointer_2 else None
    return result


# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output:9 -> 1 -> 2. That is, 912.
def sum_lists_ones_digit_at_tail(
    linked_1: LinkedList, linked_2: LinkedList
) -> LinkedList:
    """Given equal length linked lists representing positive integers with the ones digit at tail, return sum as a
    linked list.
    Args:
        linked_1 (LinkedList): first integer to be added, e.g. the integer 617 becomes 6 -> 1 -> 7
        linked_2 (LinkedList): second integer to be added, e.g. the integer 295 becomes 2 -> 9 -> 5

    Returns:
        LinkedList: sum of the two integers, e.g. the integer 912 becomes 9 -> 1 -> 2

    Raises:
        ValueError: if the value of a Node in either input LinkedList is not an integer

    >>> l1, l2 = LinkedList.listify_integer(617, True), LinkedList.listify_integer(295, True)
    >>> sum_lists_ones_digit_at_tail(l1, l2)
    <LinkedList head=<Node value=9 next.value=1> tail=<Node value=2 next=None>>
    """
    # Simple: reverse both inputs, use same functionality from before
    return sum_lists_ones_digit_at_head(
        reversed(linked_1), reversed(linked_2), returned_forwards=True
    )
    # Complex: add from left to right, but "look ahead" for whether a carried 1 will be needed


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
