class Solution:
    """link to the problem: https://leetcode.com/problems/3sum/"""
    @staticmethod
    def v1_three_sum(nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2) 1159ms beats 64.60%
        Space complexity: 0(n) 20.24mb beats 94.06%
        """
        result = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = v + nums[l] + nums[r]

                if three_sum == 0:
                    result.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
        return result
