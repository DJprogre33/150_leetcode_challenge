class Solution:
    """link to the problem: https://leetcode.com/problems/combination-sum/"""
    @staticmethod
    def v1_combination_sum(candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n^2) 58ms beats 71.10%
        Space complexity: 0(n) 16.13mb beats 99.31%
        """
        res = []

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur[:])
                return

            if idx >= len(candidates) or total > target:
                return

            cur.append(candidates[idx])
            dfs(idx, cur, total + candidates[idx])
            cur.pop()
            dfs(idx + 1, cur, total)

        dfs(0, [], 0)
        return res

    @staticmethod
    def v2_combination_sum(candidates: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n * m) 46ms beats 97.17%
        Space complexity: 0(n * m) 16.22mb beats 94.13%
        """
        # Create an array of which sums are reachable so far
        # If the sum is reachable, then place the combination in the array
        memory = [[] for i in range(target + 1)]
        memory[0] = [[]]

        # Iterate through all the candidates
        for c in candidates:
            # Check which sums are reachable by this candidate
            for s in range(c, target + 1):
                # Update the memory array if reachable
                for combo in memory[s - c]:
                    newCombo = combo.copy()
                    newCombo.append(c)
                    memory[s].append(newCombo)

        return memory[target]
