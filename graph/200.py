"""https://leetcode.com/problems/number-of-islands/"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(i: int, j: int):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == "0":
                return
            # make grid is visited
            grid[i][j] = "0"
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(x, y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                dfs(i, j)
                count += 1
        return count
