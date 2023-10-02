class Solution:
    """link to the problem: https://leetcode.com/problems/combination-sum-ii/"""
    @staticmethod
    def v1_combination_sum(candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n * n^2) 68ms beats 70.31%
        Space complexity: 0(n ^ 2) 16.4mb beats 70.17%
        """
        candidates.sort()
        res, temp = [], []

        def back_track(pos, target):
            if target == 0:
                res.append(temp[:])
                return

            if target < 0:
                return

            prev = None

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                temp.append(candidates[i])
                back_track(i + 1, target - candidates[i])
                temp.pop()
                prev = candidates[i]

        back_track(0, target)
        return res
