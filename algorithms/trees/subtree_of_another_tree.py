from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/subtree-of-another-tree/"""
    @staticmethod
    def v1_is_sub_tree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(r * s) 101ms beats 77.98%
        Space complexity: O(n) 17.52mb beats 51.74%
        """
        def is_sub_tree(root, sub_root):
            if not sub_root:
                return True
            if not root:
                return False
            if same_tree(root, sub_root):
                return True
            return is_sub_tree(root.left, sub_root) or is_sub_tree(root.right, sub_root)

        def same_tree(r, s):
            if not r and not s:
                return True
            if r and s and r.val == s.val:
                return same_tree(r.left, s.left) and same_tree(r.right, s.right)
            return False
