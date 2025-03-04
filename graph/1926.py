"""https://leetcode.com/problems/nearest-exit-from-entrance-in-maze."""
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        q = deque()
        start = tuple(entrance)
        r, c = start
        # Mark the entrance as visited
        maze[r][c] = "+"
        q.append((r, c, 0))
        while q:
            r, c, lv = q.popleft()
            # BFS guarantees that the first time you reach an exit, it is the shortest path # noqa
            if (r == 0 or r == row-1 or c == 0 or c == col-1) and (r, c) != start: # noqa
                return lv
            # get neighbors
            directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directs:
                n_r, n_c = r+dr, c+dc
                if 0 <= n_r < row and 0 <= n_c < col and maze[n_r][n_c] == ".":
                    # Mark the neighbor as visited
                    maze[n_r][n_c] = "+"
                    q.append((n_r, n_c, lv+1))
        return -1
