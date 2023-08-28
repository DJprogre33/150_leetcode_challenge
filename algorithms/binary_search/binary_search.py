class Solution:
    """link to the problem: https://leetcode.com/problems/binary-search/"""
    @staticmethod
    def v1_search(nums: list[int], target: int) -> int:
        """
        Time complexity: O(logN) 230ms beats 51.43%
        Space complexity: 0(1) 17.72mb beats 92.00%
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
