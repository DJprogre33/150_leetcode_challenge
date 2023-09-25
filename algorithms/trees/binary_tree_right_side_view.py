from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/binary-tree-right-side-view/"""
    @staticmethod
    def v1_right_side_view(root: Optional[TreeNode]) -> list[int]:
        """
        Time complexity: O(n) 38 ms beats 73.17%
        Space complexity: O(1) 16.3mb beats 33.81%
        """
        res = []
        q = deque([root])

        while q:
            right_side = None
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                if node:
                    right_side = node
                    q.extend([node.left, node.right])

            if right_side:
                res.append(right_side.val)
        return res

    @staticmethod
    def v2_right_side_view(root: Optional[TreeNode]) -> list[int]:
        """
        Time complexity: O(n) 41ms beats 50.36%
        Space complexity: O(1) 16.1mb beats 91.84%
        """
        res = []
        q = deque([root])
        while q:
            was_found = False
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if node:
                    if not was_found:
                        was_found = True
                        res.append(node.val)
                    q.extend([node.right, node.left])
        return res
