class Solution:
    """https://leetcode.com/problems/permutation-in-string/"""
    @staticmethod
    def v1_check_inclusion(s1: str, s2: str) -> bool:
        """
        Time complexity: O(26 * n) 61ms beats 89.93%
        Space complexity: 0(n) 16.50mb beats 55.17%
        """
        if len(s1) > len(s2):
            return False

        counter_s1 = {}
        for el in s1:
            counter_s1[el] = counter_s1.get(el, 0) + 1

        counter_s2 = {}
        l, r = 0, 0
        while r < len(s2):
            counter_s2[s2[r]] = counter_s2.get(s2[r], 0) + 1
            if (r - l + 1) == len(s1):
                if counter_s1 == counter_s2:
                    return True
                counter_s2[s2[l]] -= 1
                if not counter_s2[s2[l]]:
                    del counter_s2[s2[l]]
                l += 1
            r += 1
        return False

    @staticmethod
    def v2_check_inclusion(s1: str, s2: str) -> bool:
        """
        Time complexity: O(n) 75ms beats 64.50%
        Space complexity: 0(n) 16.30mb beats 98.03%
        """
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
