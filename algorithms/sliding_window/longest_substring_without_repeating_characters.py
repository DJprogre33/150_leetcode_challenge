class Solution:
    """https://leetcode.com/problems/longest-substring-without-repeating-characters/"""
    @staticmethod
    def v1_length_of_longest_substring(s: str) -> int:
        """
        Time complexity: O(n) 59ms beats 78.60%
        Space complexity: 0(n) 16.48mb beats 44.51%
        """
        res = 0
        char_set = set()
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res

    @staticmethod
    def v2_length_of_longest_substring(s: str) -> int:
        """
        Time complexity: O(n) 41ms beats 99.73%
        Space complexity: 0(n) 16.36mb beats 77.38%
        """
        start = 0
        result = 0
        lookup = {}

        for i, c in enumerate(s):
            if c in lookup and start <= lookup[c]:
                start = lookup[c] + 1
            else:
                result = max(result, i-start+1)
            lookup[c] = i
        return result
