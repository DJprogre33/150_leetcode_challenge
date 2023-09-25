from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/validate-binary-search-tree/"""
    @staticmethod
    def v1_is_valid_bst(root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n) 41ms beats 91.41%
        Space complexity: O(n) 18.64mb beats 86.20%
        """
        def dfs(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("inf"), float("-inf"))
