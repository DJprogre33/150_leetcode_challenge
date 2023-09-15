class Solution:
    """link to the problem: https://leetcode.com/problems/find-the-duplicate-number/"""
    @staticmethod
    def v1_find_duplicate(nums: list[int]) -> int:
        """
        Time complexity: O(n) 521ms beats 79.84%
        Space complexity: O(1) 30.96mb beats 82.35%
        """
        # Floyd's Tortoise and Hare (Cycle Detection)
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow
