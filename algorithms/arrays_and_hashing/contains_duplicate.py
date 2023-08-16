class Solution:
    """link to the problem: https://leetcode.com/problems/contains-duplicate/"""
    @staticmethod
    def v1_contains_duplicate(nums: list[int]) -> bool:
        """
        Time complexity: O(n) 488ms beats 80.11%
        Space complexity: 0(n) 31MB beats 43.7%
        """
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return True
            hashmap.add(n)
        return False

    @staticmethod
    def v2_contains_duplicate(nums: list[int]) -> bool:
        """
        Time complexity: O(n) 480ms beats 84.61%
        Space complexity: 0(n) 34mb beats 6.75%
        """
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] > 1:
                return True
        return False
