"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            p = max(p, prices[r]-prices[l])
            r+=1
        return p
