"""https://leetcode.com/problems/max-area-of-island/description/"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs_iterative(r: int, c: int) -> int:
            area = 0
            stack = [(r, c)]
            grid[r][c] = 0
            area+=1
            while stack:
                r, c = stack.pop() 
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        continue
                    stack.append((nr, nc))
                    grid[nr][nc] = 0
                    area+=1
            return area

        def dfs_recursive(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            # make this cell is visited
            grid[r][c] = 0
            # this cell area itself
            area = 1
            for dr, dc in directions:
                area += dfs_recursive(r+dr, c+dc)
            return area   
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                area = max(dfs_iterative(r,c), area)

        return area