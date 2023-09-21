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
    def v1_lowest_common_ancestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        """
        Time complexity: O(logn) 72ms beats 64.02%
        Space complexity: O(1) 20.89mb beats 53.96%
        """
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

    def v2_lowest_common_ancestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        """
        Time complexity: O(logn) 74ms beats 55.47%
        Space complexity: O(1) 20.68mb beats 98.33%
        """
        if p.val > root.val and q.val > root.val:
            return self.v2_lowest_common_ancestor(root.right, p, q)
        elif q.val < root.val and p.val < root.val:
            return self.v2_lowest_common_ancestor(root.left, p, q)
        else:
            return root
