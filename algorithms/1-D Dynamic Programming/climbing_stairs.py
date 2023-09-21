class Solution:
    """link to the problem: https://leetcode.com/problems/climbing-stairs/"""
    @staticmethod
    def v1_climb_stairs(n: int) -> int:
        """
        Time complexity: O(n) 29ms beats 95.65%
        Space complexity: 0(1) 16.15mb beats 88.26%
        """
        # bottom-up Dynamic problem
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one
        return one

    @staticmethod
    def v2_climb_stairs(n: int) -> int:
        """
        Time complexity: O(n) 33ms beats 84.87%
        Space complexity: 0(n) 16.35mb beats 23.99%
        """
        # memoization
        memo = {}

        def rec(n: int):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            memo[n] = rec(n - 1) + rec(n - 2)
            return memo[n]
        return rec(n)
