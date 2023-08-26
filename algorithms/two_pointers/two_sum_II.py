class Solution:
    """link to the problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""
    @staticmethod
    def v1_two_sum(numbers: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n) 116ms beats 88.04%
        Space complexity: 0(1) 17.24mb beats 58.01%
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]

            if current_sum > target:
                r -= 1
            else:
                l += 1
