class Solution:
    """link to the problem: https://leetcode.com/problems/valid-anagram/"""
    @staticmethod
    def v1_is_anagram(s: str, t: str) -> bool:
        """
        Time complexity: O(n) 59ms beats 68.96%
        Space complexity: 0(n) 16.83ms beats 62.98%
        """
        if len(s) != len(t):
            return False

        ds, dt = {}, {}

        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        return ds == dt

    @staticmethod
    def v2_is_anagram(s: str, t: str) -> bool:
        """
        Time complexity: O(n) 61ms beats 62.55%
        Space complexity: 0(1) 16.7ms beats 99.7%
        """
        if len(s) != len(t):
            return False

        counter_s = [0] * 26
        counter_t = [0] * 26

        for i in range(len(s)):
            counter_s[ord(s[i]) - ord("a")] += 1
            counter_t[ord(t[i]) - ord("a")] += 1
        return counter_s == counter_t