# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """link to the problem: https://leetcode.com/problems/reverse-linked-list/"""
    @staticmethod
    def v1_reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) 26ms beats 99.83%
        Space complexity: O(n) 17.86mb beats 72.81%
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next

        if not stack:
            return

        result = stack.pop()
        point = result

        while stack:
            point.next = stack.pop()
            point = point.next
            if not stack:
                point.next = None
        return result

    @staticmethod
    def v2_reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) 37ms beats 90.43%
        Space complexity: O(1) 17.8mb beats 96.28%
        """
        prev, curr = None, head

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next
        return prev

    def v3_reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity: O(n) 41ms beats 76.32%
        Space complexity: O(n) 22.9mb beats 10.23%
        """
        if not head:
            return None

        new_head = head

        if head.next:
            new_head = self.v3_reverse_list(new_head.next)
            head.next.next = head
        head.next = None
        return new_head

