class Solution:
    """link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""
    @staticmethod
    def v1_max_profit(prices: list[int]) -> int:
        """
        Time complexity: O(n) 839ms beats 80.88%
        Space complexity: 0(1) 27.26mb beats 91.10%
        """
        max_profit = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            max_profit = max(max_profit, p - lowest)
        return max_profit
