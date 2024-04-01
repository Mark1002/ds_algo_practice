"""
https://leetcode.com/problems/search-a-2d-matrix/.
"""
from utils import run

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Row based
        row_max_idx = len(matrix) - 1
        col_max_idx = len(matrix[0]) - 1
        start, end = 0, row_max_idx
        while start <= end:
            mid = (start + end) // 2
            min_val, max_val = matrix[mid][0], matrix[mid][col_max_idx]
            if target == min_val or target == max_val:
                print("find target at row!")
                return True
            elif target > min_val and target < max_val:
                row_idx = mid
                break
            elif target < min_val:
                end = mid - 1
                row_idx = max(end, 0)
            else:
                start = mid + 1
                row_idx = min(start, row_max_idx)
        print(f"row index: {row_idx}")
        # Column based
        row = matrix[row_idx]
        col_max_idx = len(row) - 1
        start, end = 0, col_max_idx
        while start <= end:
            mid = (start + end) // 2
            val = row[mid]
            if target == val:
                return True
            elif target < val:
                end = mid - 1
            else:
                start = mid + 1
        return False


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {
                "matrix": [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]
                ],
                "target": 3
            },
            "ans": True
        },
        {
            "input": {
                "matrix": [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 60]
                ],
                "target": 13
            },
            "ans": False
        },
        {
            "input": {
                "matrix": [
                    [1]
                ],
                "target": 2
            },
            "ans": False
        },
        {
            "input": {
                "matrix": [
                    [-22, 1, 6],
                    [12, 13, 15]
                ],
                "target": 16
            },
            "ans": False
        },
        {
            "input": {
                "matrix": [
                    [0]
                ],
                "target": 0
            },
            "ans": True
        },
    ]
    run(test_cases, s.searchMatrix)
