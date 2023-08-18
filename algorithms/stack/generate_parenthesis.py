class Solution:
    """link to the problem: https://leetcode.com/problems/generate-parentheses/"""
    @staticmethod
    def v1_generate_parenthesis(n: int) -> list[str]:
        """
        Time complexity: O(2^n) 47ms beats 58.19%
        Space complexity: 0(n) 16.57mb beats 88.17%
        """
        res = []
        stack = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res

