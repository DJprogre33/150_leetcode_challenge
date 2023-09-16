# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """link to the problem: https://leetcode.com/problems/merge-k-sorted-lists/"""

    def v1_merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time complexity: O(nlogk) 92ms beats 77.38%
        Space complexity: O(1) 19.76mb beats 98.46%
        """
        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge_lists(l1, l2))
            lists = merged_list
        return lists[0]

    @staticmethod
    def merge_lists(l1, l2):
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
