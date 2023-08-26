class Solution:
    """link to the problem: https://leetcode.com/problems/valid-palindrome/"""
    @staticmethod
    def custom_allnum(l: str) -> bool:
        return (
            ord("A") <= ord(l) <= ord("Z") or
            ord("a") <= ord(l) <= ord("z") or
            ord("0") <= ord(l) <= ord("9")
        )

    @staticmethod
    def v1_is_palindrome(s: str) -> bool:
        """
        Time complexity: O(n) 50ms beats 77.61%
        Space complexity: 0(1) 17.00mb beats 86.29%
        """
        left_idx, right_idx = 0, len(s) - 1
        while left_idx <= right_idx:
            if not s[left_idx].isalnum():
                left_idx += 1
                continue
            if not s[right_idx].isalnum():
                right_idx -= 1
                continue
            if s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx += 1
            right_idx -= 1
        return True

    def v2_is_palindrome(self, s: str) -> bool:
        """
        Time complexity: O(n) 68ms beats 26.14%
        Space complexity: 0(n) 17.06mb beats 86.29%
        """
        # same method but with using custom allnum filter
        left_idx, right_idx = 0, len(s) - 1
        while left_idx <= right_idx:
            if not self.custom_allnum(s[left_idx]):
                left_idx += 1
                continue
            if not self.custom_allnum(s[right_idx]):
                right_idx -= 1
                continue
            if s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx += 1
            right_idx -= 1
        return True
