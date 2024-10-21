"""https://leetcode.com/problems/maximum-average-subarray-i."""
import math

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = math.inf * -1
        cur_sum = 0
        l, r = 0, 0
        while r < len(nums):
            cur_sum += nums[r]
            if r-l+1 == k:
                max_avg = max(cur_sum/k, max_avg)
                cur_sum = cur_sum - nums[l]
                l += 1
            r += 1
        return max_avg
