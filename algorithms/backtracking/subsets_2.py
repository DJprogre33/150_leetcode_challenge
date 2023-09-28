class Solution:
    """link to the problem: https://leetcode.com/problems/permutations/"""
    @staticmethod
    def v1_sub_set_with_dup(nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n * n^2) 37ms beats 89.64%
        Space complexity: 0(n ^ 2) 16.50mb beats 48.26%
        """
        nums.sort()
        res = []
        subset = []

        def back_track(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return
            # all subsets that include nums[idx]
            subset.append(nums[idx])
            back_track(idx + 1)
            subset.pop()
            # all subsets thath don't include nums[idx]
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            back_track(idx + 1)
        back_track(0)
        return res

    @staticmethod
    def v2_sub_set_with_dup(nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n * n^2) 38ms beats 85.37%
        Space complexity: 0(n ^ 2) 16.50mb beats 78.31%
        """
        res = []
        subset = []

        def back_track(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return
            # all subsets that include nums[idx]
            subset.append(nums[idx])
            back_track(idx + 1)
            n = subset.pop()
            if n in subset:
                return
            back_track(idx + 1)
        back_track(0)
        return res
