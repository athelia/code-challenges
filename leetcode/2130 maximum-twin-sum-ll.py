# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # first get the length
        # then from the length, get the midpoint
        # then from the midpoint, reverse the second half of the ll
        # then sum ll[i] + ll[i+n/2] to get max

        # with 2 pointers, get midpoint
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        head_reversed_second_half = reverse_ll(slow)
        result = 0
        node1 = head
        node2 = head_reversed_second_half
        while node2:
            current_total = node1.val + node2.val
            result = current_total if current_total > result else result
            node1 = node1.next
            node2 = node2.next
        return result


# 5 -> 4 -> 2 -> 1 -> None
# slow  fast
# 5     5
# 4     2
# 2     None

# 5 -> 4 -> 1 -> 2 -> None


def reverse_ll(head: Optional[ListNode]) -> ListNode:
    # iterate to the right, but adjust .nexts to point "to the left"
    current = head
    new_previous = None
    while current:
        new_current = current.next
        current.next = new_previous
        new_previous = current
        current = new_current
    return new_previous


# a -> b -> c -> d -> None
# cur   n_prev  n_cur   c.nxt   n_prev  current
# a     None    b       None    a       b
# b     a       c       a       b       c
# c     b       d       b       c       d
# d     c       None    c       d       None
# end
# a -> None
# b -> a
# c -> b
# d -> c

# goal:
# None <- a
# a <- b
# b <- c
# c <- d
# d <- head


def reverse_ll_2(head: Optional[ListNode]) -> ListNode:
    left, current = None, head
    while current:
        right = current.next
        current.next = left
        left = current
        current = right
    return left
