class Solution:
    """link to the problem: https://leetcode.com/problems/longest-consecutive-sequence/"""
    @staticmethod
    def v1_longest_consecutive(nums: list[int]) -> int:
        """
        Time complexity: O(n) 1474ms beats 41.17%
        Space complexity: 0(n) 31.2mb beats 52.16%
        """
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest

    @staticmethod
    def v2_longest_consecutive(nums: list[int]) -> int:
        """
        Time complexity: O(n) 375ms beats 87.42%
        Space complexity: 0(n) 31.1mb beats 52.16%
        """
        uniques = set(nums)
        max_length = 0

        while uniques:
            low = high = uniques.pop()
            # check values in two ways
            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1

                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)
        return max_length
