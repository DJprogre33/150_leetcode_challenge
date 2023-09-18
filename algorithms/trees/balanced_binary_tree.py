from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/balanced-binary-tree/"""
    @staticmethod
    def v1_is_balanced(root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n) 47ms beats 88.45%
        Space complexity: O(1) 20.95mb beats 93.76%
        """
        is_balanced = True

        def dfs(root):
            nonlocal is_balanced

            if not root:
                return 0

            left_h, right_h = dfs(root.left), dfs(root.right)
            if abs(right_h - left_h) > 1:
                is_balanced = False

            return 1 + max(left_h, right_h)

        dfs(root)
        return is_balanced
