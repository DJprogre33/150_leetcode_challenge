from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/"""
    @staticmethod
    def max_path_sum(root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n) 69ms beats 93.84%
        Space complexity: O(n) 23.73mb beats 79.29%
        """
        max_sum = root.val

        # return max path sum w/o splitting
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            # do not take into account branches with negative path sum
            left_max, right_max = dfs(root.left), dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            # compute max path sum with split
            max_sum = max(max_sum, root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return max_sum
