class Solution:
    """https://leetcode.com/problems/longest-repeating-character-replacement/"""
    @staticmethod
    def v1_character_replacement(s: str, k: int) -> int:
        """
        Time complexity: O(n) 125ms beats 51.41%
        Space complexity: 0(n) 16.41mb beats 40.25%
        """
        counter = {}
        res = 0

        left = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

    @staticmethod
    def v2_character_replacement(s: str, k: int) -> int:
        """
        Time complexity: O(n) 88ms beats 87.14%
        Space complexity: 0(n) 16.39mb beats 73.73%
        """
        counter = {}
        res = 0

        left = 0
        max_freq = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_freq = max(max_freq, counter[s[right]])
            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
