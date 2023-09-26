from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CodecV1:
    """
    Time complexity: O(n) 102ms beats 72.49%
    Space complexity: O(n) 22.39mb beats 69.42%
    """
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        res = ""
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res += f" {str(node.val)}"
                    q.extend([node.left, node.right])
                else:
                    res += " None"
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        nodes = deque(data.split())
        if nodes and nodes[0] != "None":
            root = TreeNode(int(nodes.popleft()))
            q = deque([root])
            while q:
                node = q.popleft()
                if node:
                    n_left, n_right = nodes.popleft(), nodes.popleft()
                    node.left = TreeNode(int(n_left)) if n_left != "None" else None
                    node.right = TreeNode(int(n_right)) if n_right != "None" else None
                    q.extend([node.left, node.right])
            return root


class CodecV2:
    """
    Time complexity: O(n) 100ms beats 78.95%
    Space complexity: O(n) 22.39mb beats 69.42%
    """
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def dfs(root):
            if not root:
                return "None"
            return str(root.val) + " " + root.left + " " + root.right
        res = dfs(root)
        print(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        values = data.split()
        idx = 0
        def dfs():
            nonlocal idx
            if values[idx] == "None":
                idx += 1
                return None

            node = TreeNode(int(values[idx]))
            idx += idx
            node.left, node.right = dfs(), dfs()
            return node
        return dfs()
