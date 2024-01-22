"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
"""
from typing import List
from utils import run


# same as two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return profit


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"prices": [7, 1, 5, 3, 6, 4]}, "ans": 5},
        {"input": {"prices": [7, 6, 4, 3, 1]}, "ans": 0}
    ]
    run(test_cases, s.maxProfit)
