"""https://leetcode.com/problems/number-of-islands/"""
from typing import List
from collections import deque

class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
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
    
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
    
        def bfs(r: int, c: int):
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            rows, cols = len(grid), len(grid[0])
            queue = deque()
            queue.append((r, c))
            # make as visited
            grid[r][c] = "0"

            while queue:
                r, c = queue.popleft()
                for dr, dc in direction:
                    nr, nc = r+dr, c+dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        # make as visited 
                        grid[nr][nc] = "0"

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    continue
                bfs(i, j)
                # finish traversal means find a island
                count+=1
        return count
