"""
https://leetcode.com/problems/binary-search/
"""
from utils import run

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(start: int, end: int) -> int:
            mid = (start + end) // 2
            if start == end and nums[mid] != target:
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] > target:  # left
                return bin_search(start, max(mid - 1, 0))
            if nums[mid] < target:  # right
                return bin_search(min(mid + 1, len(nums)-1), end)

        return bin_search(0, len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {
                "nums": [-1, 0, 3, 5, 9, 12],
                "target": 9,
            },
            "ans": 4
        },
        {
            "input": {
                "nums": [-1, 0, 3, 5, 9, 12],
                "target": 2,
            },
            "ans": -1
        },
        {
            "input": {
                "nums": [-11, -10],
                "target": -110,
            },
            "ans": -1
        }
    ]
    run(test_cases, s.search)
