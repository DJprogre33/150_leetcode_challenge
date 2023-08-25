class Solution:
    """link to the problem: https://leetcode.com/problems/largest-rectangle-in-histogram/"""
    @staticmethod
    def v1_largest_rectangle_area(heights: list[int]) -> int:
        """
        Time complexity: O(n) 756ms beats 87.21%
        Space complexity: 0(n) 33.10mb beats 43.66%
        """
        stack = []
        max_value = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                max_value = max(max_value, popped_h * (i - popped_i))
                start = popped_i
            stack.append((start, h))

        for i, h in stack:
            max_value = max(max_value, h * (len(heights) - i))

        return max_value

    @staticmethod
    def v2_largest_rectangle_area(heights: list[int]) -> int:
        """
        Time complexity: O(n) 724ms beats 98.51%
        Space complexity: O(n) 30.62mb beats 72.75%
        """
        stack, max_value = [], 0
        for bar in heights + [-1]:  # add -1 to have an additional iteration
            step = 0
            while stack and stack[-1][1] >= bar:
                width, height = stack.pop()
                step += width
                max_value = max(max_value, step * height)

            stack.append((step + 1, bar))
        return max_value
