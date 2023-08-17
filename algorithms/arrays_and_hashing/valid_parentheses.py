class Solution:
    """link to the problem: https://leetcode.com/problems/valid-parentheses/"""
    @staticmethod
    def v1_is_valid(s: str) -> bool:
        """
        Time complexity: O(n) 41ms beats 71.74%
        Space complexity: 0(n) 16.31mb beats 52.98%
        """
        if len(s) % 2 != 0:
            return False

        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack.pop() != hashmap[c]:
                    return False
        return not stack
