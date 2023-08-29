class Solution:
    """link to the problem: https://leetcode.com/problems/binary-search/"""
    @staticmethod
    def v1_search_matrix(matrix: list[list[int]], target: int) -> bool:
        """
        Time complexity: O(log(m * n)) 44ms beats 91.57%
        Space complexity: 0(1) 16.9mb beats 20.40%
        """
        for row in matrix:
            left, right = 0, len(row) - 1

            if not row[left] <= target <= row[right]:
                continue
            else:
                while left <= right:
                    mid = left + (right - left) // 2

                    if row[mid] == target:
                        return True

                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False

    @staticmethod
    def v2_search_matrix(matrix: list[list[int]], target: int) -> bool:
        """
        Time complexity: O(log(m) + log(n)) 48ms beats 77.64%
        Space complexity: 0(1) 16.85mb beats 58.01%
        """
        top_row, bottom_row = 0, len(matrix) - 1

        while top_row <= bottom_row:
            mid_row = top_row + (bottom_row - top_row) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = matrix[mid_row]
                left, right = 0, len(target_row) - 1

                while left <= right:
                    mid = left + (right - left) // 2

                    if target_row[mid] == target:
                        return True

                    if target_row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            else:
                bottom_row = mid_row - 1
        return False
