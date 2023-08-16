from collections import defaultdict

class Solution:
    """link to the problem: https://leetcode.com/problems/valid-sudoku/"""
    @staticmethod
    def v1_valid_sudoku(board: list[list[int]]) -> bool:
        """
        Time complexity: O(n) 95ms beats 96.06%
        Space complexity: 0(n) 16.30mb beats 80.95%
        """
        hashmap = {}
        for i in range(9):
            # track each line
            ox = set()
            oy = set()
            for j in range(9):
                square_num = (i // 3, j // 3)
                number_ox = board[i][j]
                number_oy = board[j][i]

                hashmap.setdefault(square_num, [])

                if number_ox != ".":
                    if number_ox in hashmap[square_num]:
                        return False
                    hashmap[square_num] = hashmap[square_num] + [square_num]
                    if number_ox in ox:
                        return False
                if number_oy != "." and number_oy in oy:
                    return False
                ox.add(number_ox)
                oy.add(number_oy)
        return True

    @staticmethod
    def v2_valid_sudoku(board: list[list[int]]) -> bool:
        """
        Time complexity: O(n) 97ms beats 93.69%
        Space complexity: 0(n) 16.34mb beats 52.11%
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[r//3, c//3]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True

