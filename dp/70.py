"""https://leetcode.com/problems/climbing-stairs."""

from typing import List
from utils import run


class Solution:
    def climbStairsTopDown(self, n: int) -> int:
        dp = [None] * (n+1)

        def climb(n: int, dp: List[int]) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n]:
                return dp[n]
            dp[n] = climb(n-1, dp) + climb(n-2, dp)
            return dp[n]
        return climb(n, dp)

    def climbStairsBottomUp(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"n": 8}, "ans": 34}
    ]
    for func in [s.climbStairsBottomUp, s.climbStairsTopDown]:
        run(test_cases, func)
