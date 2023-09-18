from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/diameter-of-binary-tree/"""
    @staticmethod
    def v1_diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n) 46ms beats 76.73%
        Space complexity: O(1) 18.58mb beats 91.49%
        """
        diameter = 0

        def dfs(root):
            nonlocal diameter
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter
