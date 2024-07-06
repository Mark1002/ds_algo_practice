"""https://leetcode.com/problems/min-cost-climbing-stairs/."""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [None] * (len(cost) + 3)

        def climb(i):
            if dp[i+1] is not None:
                return dp[i+1]
            if i >= len(cost):
                return 0
            min_cost = (0 if i < 0 else cost[i]) + min(climb(i+1), climb(i+2))
            dp[i+1] = min_cost
            return dp[i+1]

        return climb(-1)
