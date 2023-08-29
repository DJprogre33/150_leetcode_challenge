import math


class Solution:
    """link to the problem: https://leetcode.com/problems/koko-eating-bananas/"""
    @staticmethod
    def v1_min_eating_speed(piles: list[int], h: int) -> int:
        """
        Time complexity: O(log(max(piles)) * O(n) 370ms beats 67.5%
        Space complexity: 0(1) 17.9mb beats 45.56%
        """
        left, right = 1, max(piles)
        eating_speed = right

        while left <= right:
            mid = left + (right - left) // 2
            current_speed = 0
            for p in piles:
                current_speed += math.ceil(p / mid)

            if current_speed > h:
                left = mid + 1
            else:
                eating_speed = mid
                right = mid - 1
        return eating_speed
