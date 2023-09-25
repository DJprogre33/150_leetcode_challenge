from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/"""
    @staticmethod
    def v1_good_nodes(root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n) 193ms beats 51.16%
        Space complexity: O(n) 34.89mb beats 97.31%
        """
        def dfs(node, max_value):
            if not node:
                return 0

            res = 1 if node.val >= max_value else 0
            max_value = max(max_value, res)
            res += dfs(node.left, max_value) + dfs(node.right, max_value)
            return res
        return dfs(root, root.val)

    @staticmethod
    def v2_good_nodes(root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n) 167ms beats 97.37%
        Space complexity: O(n) 34.90mb beats 97.31%
        """
        good_counter = 0

        def dfs(node, max_value):
            nonlocal good_counter

            if not node:
                return
            if node.val >= max_value:
                good_counter += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, root.val)
        return good_counter

    @staticmethod
    def v3_good_nodes(root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n) 201ms beats 31.95%
        Space complexity: O(n) 35.46mb beats 5.26%
        """
        total_good = 0
        q = deque([(root, root.val)])
        while q:
            node, max_in_path = q.popleft()
            if node:
                if node.val >= max_in_path:
                    max_in_path = node.val
                    total_good += 1
                q.extend([(node.left, max_in_path), (node.right, max_in_path)])
            return total_good
