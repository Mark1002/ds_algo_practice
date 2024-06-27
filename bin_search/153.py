"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array"""
from typing import List
from utils import run


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:  # prevent infinite loop
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {
                "nums": [4, 5, 6, 7, 0, 1, 2]
            },
            "ans": 0
        }
    ]
    run(test_cases, s.findMin)
