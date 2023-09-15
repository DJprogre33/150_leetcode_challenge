# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """link to the problem: https://leetcode.com/problems/linked-list-cycle/description/"""
    @staticmethod
    def v1_add_two_numbers(head: Optional[ListNode]) -> bool:
        """
        Time complexity: O(n) 51ms beats 90.14%
        Space complexity: O(1) 20.28mb beats 87.55%
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

