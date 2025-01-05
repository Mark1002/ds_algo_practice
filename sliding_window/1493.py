# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        zero_idx = None
        result = 0
        while r < len(nums):
            if nums[r] == 0:
                # zero was seen before
                if zero_idx is not None:
                    l = zero_idx + 1
                zero_idx = r
            result = max(result, r-l)
            r += 1
        return result
