class Solution:
    """link to the problem: https://leetcode.com/problems/trapping-rain-water/"""
    @staticmethod
    def v1_trap(height: list[int]) -> int:
        """
        Time complexity: O(n) 109ms beats 87.44%
        Space complexity: 0(1) 18.19mb beats 87.59%
        """
        trapped = 0

        if len(height) <= 2:
            return trapped

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped += right_max - height[right]
        return trapped
