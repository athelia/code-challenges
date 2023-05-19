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
        length = 0
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


def reverse_ll(head: Optional[ListNode]) -> ListNode:
    current = head
    while current:
        current.next.next = current
        # WIP
    return current

# 5 -> 4 -> 2 -> 1 -> None
# slow  fast
# 5     5
# 4     2
# 2     None
