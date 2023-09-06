"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_count = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 in num_set:
                continue
            i = num
            count = 0
            while i in num_set:
                count += 1
                i += 1
            long_count = max(long_count, count)
        return long_count


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": [100, 4, 200, 1, 3, 2], "ans": 4},
        {"input": [], "ans": 0},
        {"input": [-6, -5, -9, 11, -7, 10, 13, -8, 9, 12, -4], "ans": 6},
        {"input": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], "ans": 9},
    ]
    for test_case in test_cases:
        assert s.longestConsecutive(test_case["input"]) == test_case["ans"]
