# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """link to the problem: https://leetcode.com/problems/merge-two-sorted-lists/"""
    @staticmethod
    def v1_merge_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) 38ms beats 90.91%
        Space complexity: O(1) 16.38mb beats 48.53%
        """
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dummy.next
