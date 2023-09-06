class Solution:
    """https://leetcode.com/problems/minimum-window-substring/"""
    @staticmethod
    def v1_min_window(s: str, t: str) -> str:
        """
        Time complexity: O(n) 101ms beats 86.40%
        Space complexity: 0(n) 17.15mb beats 59.43%
        """
        if t == "":
            return ""

        count_t, window = {}, {}
        res, res_len = [-1, -1], float("infinity")
        l = 0

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        left, right = res

        if res_len < float("infinity"):
            return s[left: right + 1]
        else:
            return ""
