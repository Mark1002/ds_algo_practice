"""
url: https://leetcode.com/problems/valid-sudoku/description/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row and column
        for r in range(9):
            d = set()
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                if n in d:
                    return False
                d.add(n)
        # check column
        for r in range(9):
            d = set()
            for c in range(9):
                n = board[c][r]
                if n == ".":
                    continue
                if n in d:
                    return False
                d.add(n)
        # check sub-box
        for r in range(1, 8, 3):
            for c in range(1, 8, 3):
                d = set()
                sub_box = [
                    board[r-1][c-1], board[r-1][c], board[r-1][c+1],
                    board[r][c-1], board[r][c], board[r][c+1],
                    board[r+1][c-1],board[r+1][c], board[r+1][c+1],
                ]
                for n in sub_box:
                    if n == ".":
                        continue
                    if n in d:
                        return False
                    d.add(n)
        return True


if __name__ == "__main__":
    s = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(s.isValidSudoku(board))
