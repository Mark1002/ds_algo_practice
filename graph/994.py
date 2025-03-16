"""https://leetcode.com/problems/rotting-oranges."""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0
        lv = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    q.append((i, j, lv))

        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            s_r, s_c, lv = q.popleft()
            for r, c in directs:
                n_r, n_c = s_r+r, s_c+c
                if 0 <= n_r < row and 0 <= n_c < col and grid[n_r][n_c] == 1:
                    grid[n_r][n_c] = 2
                    fresh_count -= 1
                    q.append((n_r, n_c, lv+1))
        if fresh_count == 0:
            return lv
        return -1
