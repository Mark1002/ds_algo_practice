"""https://leetcode.com/problems/house-robber"""
from typing import List
from utils import run


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = num
            elif i == 1:
                dp[i] = max(dp[i-1], num)
            else:
                dp[i] = max(dp[i-1], dp[i-2]+num)
        return dp[len(nums)-1]

    def improveRob(self, nums: List[int]) -> int:
        # 只有用到兩個變數，可以把 dp array 空間優化
        prev1, prev2 = 0, 0
        for num in nums:
            temp = max(prev2, prev1 + num)
            prev1 = prev2
            prev2 = temp
        return prev2


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {"nums": [2, 7, 9, 3, 1]},
            "ans": 12
        }
    ]
    run(test_cases, s.improveRob)
