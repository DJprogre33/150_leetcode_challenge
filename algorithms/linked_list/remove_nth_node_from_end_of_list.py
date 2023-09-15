# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """link to the problem: https://leetcode.com/problems/reorder-list/"""
    @staticmethod
    def v1_remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time complexity: O(n) 38ms beats 78.06%
        Space complexity: O(1) 16.28mb beats 68.87%
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
