class Solution:
    """link to the problem: https://leetcode.com/problems/search-in-rotated-sorted-array/"""
    @staticmethod
    def v1_search(nums: list[int], target: int) -> int:
        """
        Time complexity: O(logN) 48ms beats 63.72%
        Space complexity: 0(1) 16.70mb beats 69.06%
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if not nums[left] <= target <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if not nums[mid] <= target <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
