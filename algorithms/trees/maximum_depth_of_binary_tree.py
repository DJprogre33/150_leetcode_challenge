from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/"""

    def v1_max_depth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS
        """
        Time complexity: O(n) 50ms beats 38.99%
        Space complexity: O(n) 18.5mb beats 75.86%
        """
        if not root:
            return 0
        return 1 + max(self.v1_max_depth(root.left), self.v1_max_depth(root.right))

    @staticmethod
    def v2_max_depth(self, root: Optional[TreeNode]) -> int:
        # BFS using queue
        """
        Time complexity: O(n) 41ms beats 87.90%
        Space complexity: O(n) 17.46 mb beats 99.74%
        """
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    @staticmethod
    def v2_max_depth(self, root: Optional[TreeNode]) -> int:
        # BFS using queue
        """
        Time complexity: O(n) 41ms beats 87.90%
        Space complexity: O(n) 17.46 mb beats 99.74%
        """
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    @staticmethod
    def v3_max_depth(self, root: Optional[TreeNode]) -> int:
        # DFS using stack
        """
        Time complexity: O(n) 45ms beats 70.78%
        Space complexity: O(n) 17.6 mb beats 89.80%
        """
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
