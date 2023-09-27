class Solution:
    """link to the problem: https://leetcode.com/problems/permutations/"""
    @staticmethod
    def v1_permute(nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n^2) ms beats %
        Space complexity: 0(n) mb beats %
        """
        res = []

        def back_track(i):
            if i >= len(nums):
                res.append(nums[:])

            for p in range(i, len(nums)):
                nums[i], nums[p] = nums[p], nums[i]
                back_track(i + 1)
                nums[i], nums[p] = nums[p], nums[i]

        back_track(0)
        return res

