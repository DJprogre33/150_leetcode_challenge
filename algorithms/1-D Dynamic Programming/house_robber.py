class Solution:
    """link to the problem: https://leetcode.com/problems/house-robber/"""
    @staticmethod
    def v1_rob(nums: list[int]) -> int:
        """
        Time complexity: O(n) 40ms beats 53.13%
        Space complexity: 0(1) mb beats 99.95%
        """
        nums += [0, 0, 0]

        for i in range(len(nums) - 4, -1, -1):
            nums[i] += max(nums[i + 2], nums[i + 3])
        return max(nums[0], nums[1])

    @staticmethod
    def v2_rob(nums: list[int]) -> int:
        """
        Time complexity: O(n) 38ms beats 69.39%
        Space complexity: 0(1) mb beats 99.13%
        """
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            rob2, rob1 = max(n + rob1, rob2), rob2
        return rob2
