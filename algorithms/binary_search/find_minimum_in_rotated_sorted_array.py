class Solution:
    """link to the problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""
    @staticmethod
    def v1_find_min(nums: list[int]) -> int:
        """
        Time complexity: O(logN) 50ms beats 58.34%
        Space complexity: 0(1) 16.58mb beats 78.49%
        """
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = left + (right - left) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res
