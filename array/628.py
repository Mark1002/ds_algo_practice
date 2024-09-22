"""https://leetcode.com/problems/maximum-product-of-three-numbers."""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        negative = []
        positive = []
        res1 = res2 = res3 = res4 = float("-inf")
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        negative.sort()
        positive.sort(reverse=True)
        # +++
        if len(positive) >= 3:
            res1 = positive[0] * positive[1] * positive[2]
        # --+
        if len(negative) >= 2 and len(positive) >= 1:
            res2 = positive[0] * negative[0] * negative[1]
        # ++-
        if len(negative) >= 1 and len(positive) >= 2:
            res3 = positive[0] * positive[1] * negative[0]
        # ---
        if len(negative) >= 3:
            res4 = negative[-1] * negative[-2] * negative[-3]
        return max(res1, res2, res3, res4)
