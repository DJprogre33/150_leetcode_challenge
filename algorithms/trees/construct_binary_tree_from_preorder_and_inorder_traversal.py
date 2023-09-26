from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """link to the problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"""
    @staticmethod
    def v1_build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Time complexity: O(n) 163ms beats 53.97%
        Space complexity: O(n) 90.9mb beats 13.45%
        """
        def recursive(preorder: list[int], inorder: list[int]):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = recursive(preorder[1:mid + 1], inorder[:mid])
            root.right = recursive(preorder[mid + 1:], inorder[mid + 1:])
            return root
        return recursive(preorder, inorder)

    @staticmethod
    def v2_build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Time complexity: O(n) 54ms beats 96.41%
        Space complexity: O(n) 21.06mb beats 86.75%
        """
        inorder_map = {v: i for i, v in enumerate(inorder)}
        preorder_idx = 0

        def recursive(left, right):
            nonlocal preorder_idx
            if left > right:
                return None

            node_val = preorder[preorder_idx]
            root = TreeNode(node_val)
            preorder_idx += 1

            inorder_idx = inorder_map[node_val]
            root.left = recursive(left, inorder_idx - 1)
            root.right = recursive(inorder_idx + 1, right)
            return root
        return recursive(0, len(preorder) - 1)
