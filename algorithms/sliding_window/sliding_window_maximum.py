import collections


class Solution:
    """https://leetcode.com/problems/sliding-window-maximum/"""
    @staticmethod
    def max_sliding_window(nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n) 1338ms beats 61.40%
        Space complexity: 0(n) 33.24mb beats 47.65%
        """
        result = []
        q = collections.deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            r += 1
        return result