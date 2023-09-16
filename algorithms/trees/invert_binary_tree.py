from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/invert-binary-tree/"""

    def v1_invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n) 32ms beats 92.24%
        Space complexity: O(n) 16.1mb beats 92.4%
        """
        # using DFS
        if not root:
            return None
        root.left, root.right = self.v1_invert_tree(root.right), self.v1_invert_tree(root.left)
        return root

    @staticmethod
    def v2_invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n) 33ms beats 90.75%
        Space complexity: O(n) 16.18mb beats 92.04%
        """
        # using BFS
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root
