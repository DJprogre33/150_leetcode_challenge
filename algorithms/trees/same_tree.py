from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/same-tree/"""
    @staticmethod
    def v1_is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n) 32ms beats 91.46%
        Space complexity: O(n) 16.22mb beats 83.49%
        """
        queue = deque([p, q])

        while queue:
            node_p, node_q = queue.popleft(), queue.popleft()
            if node_q and node_p:
                if node_q.val != node_p.val:
                    return False
                queue.extend([node_p.left, node_q.left, node_p.right, node_q.right])
            else:
                if node_q != node_p:
                    return False
        return True

    @staticmethod
    def v2_is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n) 35ms beats 78.96%
        Space complexity: O(n) 16.09 mb beats 99.92%
        """
        def dfs(p, q):
            if not p and not q:
                return True
            if (not p or not q) or (p.val != q.val):
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)
