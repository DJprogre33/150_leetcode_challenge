class Solution:
    """link to the problem: https://leetcode.com/problems/two-sum/"""
    @staticmethod
    def v1_two_sum(nums: list, target: int) -> list[int]:
        """
        Time complexity: O(n) 62ms beats 91.45%
        Space complexity: 0(n) 17.8mb beats 14.76%
        """
        hashmap = {}
        for i, v in enumerate(nums):
            if v in hashmap:
                return [hashmap[v], i]
            hashmap[target - v] = i
