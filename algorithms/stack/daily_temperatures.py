class Solution:
    """link to the problem: https://leetcode.com/problems/daily-temperatures/"""
    @staticmethod
    def v1_daily_temperatures(temperatures: list[int]) -> list[int]:
        """
        Time complexity: O(n) 1046ms beats 92.23%
        Space complexity: 0(n) 30.81mb beats 63.17%
        """
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append((t, i))
        return res
