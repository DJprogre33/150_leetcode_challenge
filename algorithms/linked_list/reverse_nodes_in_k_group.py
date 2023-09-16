# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """link to the problem: https://leetcode.com/problems/reverse-nodes-in-k-group/"""

    def v1_reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time complexity: O(n) 42ms beats 97.19%
        Space complexity: O(1) 17.26mb beats 98.89%
        """
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        return dummy.next

    @staticmethod
    def get_kth(curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr
