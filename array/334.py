"""https://leetcode.com/problems/increasing-triplet-subsequence/"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        # 不求精確的 i, j ,k 只檢查有無 i < j < k 關係存在
        for num in nums:
            # Find more smaller first
            if num <= first:
                first = num
            # num > first, find more smaller second
            elif num <= second:
                second = num
            # first < second < num
            else:
                return True
        return False
