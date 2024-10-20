"""https://leetcode.com/problems/word-search"""
from typing import List
from utils import run


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.seen = [[False] * n for _ in range(m)]

        def check_four(w_s: int, i: int, j: int) -> bool:
            if w_s == len(word):
                return True
            char = word[w_s]
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != char:
                return False
            # Mark the cell as visited by changing its value temporarily
            temp = board[i][j]
            board[i][j] = "#"
            found = (
                check_four(w_s+1, i-1, j) or
                check_four(w_s+1, i+1, j) or
                check_four(w_s+1, i, j-1) or
                check_four(w_s+1, i, j+1)
            )
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and check_four(0, i, j):
                    return True
        return False


if __name__ == "__main__":
    test_cases = [
        {
            "input": {"board": [["a", "z"], ["m", "s"]], "word": "zsm"},
            "ans": True
        },
        {
            "input": {
                "board": [
                    ["A", "B", "C", "E"],
                    ["S", "F", "C", "S"],
                    ["A", "D", "E", "E"]
                ],
                "word": "ABCB"
            },
            "ans": False
        }
    ]
    s = Solution()
    run(test_cases, s.exist)
