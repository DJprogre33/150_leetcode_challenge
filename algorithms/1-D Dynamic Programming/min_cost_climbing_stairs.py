class Solution:
    """link to the problem: https://leetcode.com/problems/min-cost-climbing-stairs/"""
    @staticmethod
    def v1_min_cost_climbing_stairs(cost: list[int]) -> int:
        """
        Time complexity: O(n) 50ms beats 97.32%
        Space complexity: 0(1) 16.44mb beats 61.78%
        """
        # bottom-up Dynamic problem
        cost += [0]

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
