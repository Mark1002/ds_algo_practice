"""https://leetcode.com/problems/longest-increasing-subsequence"""
from typing import List
from utils import run


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [None] * len(nums)

        def LIS(n: int) -> int:
            if dp[n]:
                return dp[n]
            max_len = 1
            for i in range(n+1, len(nums)):
                if nums[n] < nums[i]:
                    max_len = max(LIS(i)+1, max_len)
            dp[n] = max_len
            return max_len
        return max([LIS(i) for i in range(len(nums))])


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"nums": [10, 9, 2, 5, 3, 7, 101, 18]}, "ans": 4}
    ]
    run(test_cases, s.lengthOfLIS)
