from collections import defaultdict


class Solution:
    """link to the problem: https://leetcode.com/problems/group-anagrams/"""
    @staticmethod
    def v1_group_anagrams(strs: list[str]) -> list[list[int]]:
        """
        Time complexity: O(n) 93ms beats 94.37%
        Space complexity: 0(n) 22.20mb beats 26.53%
        """
        hashmap = {}

        for string in strs:
            count = [0] * 26
            for cymb in string:
                count[ord(cymb) - ord("a")] += 1
            hashmap.setdefault(tuple(count), []).append(string)
        return hashmap.values()

    @staticmethod
    def v2_group_anagrams(strs: list[str]) -> list[list[int]]:
        """
        Time complexity: O(n) 88ms beats 98.05%
        Space complexity: 0(n) 20.10mb beats 60.42%
        """
        hashmap = {}

        for string in strs:
            hashmap.setdefault("".join(sorted(string)), []).append(string)
        return hashmap.values()
