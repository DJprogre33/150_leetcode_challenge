
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """link to the problem: https://leetcode.com/problems/copy-list-with-random-pointer/"""
    @staticmethod
    def v1_copy_random_list(head: Optional[Node]) -> Optional[Node]:
        """
        Time complexity: O(n) 31ms beats 98.36%
        Space complexity: O(1) 17.05mb beats 99.48%
        """
        hashmap = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap.get(curr.next)
            copy.random = hashmap.get(curr.random)
            curr = curr.next

        return hashmap.get(head)
