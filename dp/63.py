"""https://leetcode.com/problems/unique-paths-ii/."""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # init first col
        flag = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                flag = 0
            dp[i][0] = flag
        # init first row
        flag = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                flag = 0
            dp[0][j] = flag

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
