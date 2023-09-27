class Solution:
    """link to the problem: https://leetcode.com/problems/subsets/"""
    @staticmethod
    def v1_subsets(nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(2^n) 35ms beats 88.70%
        Space complexity: 0(n) 16.36mb beats 91.50%
        """
        res, subset = [], []

        def dfs(i):
            if i >= len(res):
                res.append(subset[:])
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
