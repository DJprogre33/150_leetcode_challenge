from collections import deque

class Solution:
    """link to the problem: https://leetcode.com/problems/car-fleet/"""
    @staticmethod
    def v1_car_fleet(target: int, position: list[int], speed: list[int]) -> int:
        """
        Time complexity: O(nlog(n)) 733ms beats 93.35%
        Space complexity: 0(n) 39.53mb beats 20.69%
        """
        pairs = list(sorted(zip(position, speed)))[::-1]
        stack = []

        for p, s in pairs:
            # append finish time
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
