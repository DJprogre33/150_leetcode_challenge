from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/"""
    @staticmethod
    def v1_kth_smallest(root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity: O(n) 50ms beats 77.09%
        Space complexity: O(n) 20.37mb beats 81.34%
        """
        # iterative dfs using stack
        stack = []
        res = None
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val
            curr = curr.right

    @staticmethod
    def v2_kth_smallest(root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity: O(n) 51ms beats 71.76%
        Space complexity: O(n) 20.34mb beats 81.34%
        """
        res, pos = None, 1

        def inorder(root):
            nonlocal res, pos
            if not root:
                return

            inorder(root.left)

            if pos > k:
                return
            if pos == k:
                res = root.val
            pos += 1
            inorder(root.right)
        inorder(root)
        return res
