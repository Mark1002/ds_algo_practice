"""https://leetcode.com/problems/find-pivot-index."""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums)
        for i in range(len(nums)):
            r_sum = r_sum - nums[i]
            if l_sum == r_sum:
                return i
            l_sum = l_sum + nums[i]
        return -1
