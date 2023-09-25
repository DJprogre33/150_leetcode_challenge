from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/binary-tree-level-order-traversal/"""
    @staticmethod
    def v1_level_order(root: Optional[TreeNode]) -> list[list[int]]:
        """
        Time complexity: O(n) 38ms beats 91.07%
        Space complexity: O(n) 17.09mb beats 59.89%
        """
        res = []
        queue = deque([root])
        # add counter to every lvl (lets suppose that we have all nodes on every lvl)
        level_count = 1
        while queue:
            level_nodes = []
            temp_count = level_count

            while temp_count and queue:
                node = queue.popleft()
                if node:
                    level_nodes.append(node.val)
                    queue.extend([node.left, node.right])
                else:
                    # if not node decrease level_count
                    level_count -= 1
                temp_count -= 1
            # used for the last iter where all nodes are None
            if level_nodes:
                res.append(level_nodes)
            level_count *= 2
        return res

    @staticmethod
    def v2_level_order(root: Optional[TreeNode]) -> list[list[int]]:
        """
        Time complexity: O(n) 36ms beats 94.77%
        Space complexity: O(n) 16.76mb beats 99.84%
        """
        res = []
        q = deque([root])

        while q:
            q_len = len(q)
            level = []
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.extend([node.left, node.right])
            if level:
                res.append(level)
        return res
