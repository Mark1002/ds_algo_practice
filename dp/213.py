"""https://leetcode.com/problems/house-robber-ii."""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper_rob(nums: List[int]) -> int:
            prev1, prev2 = 0, 0
            for num in nums:
                temp = max(prev2, prev1 + num)
                prev1 = prev2
                prev2 = temp
            return prev2

        if len(nums) == 1:
            return nums[0]
        return max(helper_rob(nums[1:]), helper_rob(nums[:-1]))
