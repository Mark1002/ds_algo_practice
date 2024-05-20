"""https://leetcode.com/problems/koko-eating-bananas/"""
import math
from typing import List
from utils import run


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if self._find_hour_by_speed(piles, mid, h):
                right = mid - 1
                res = min(mid, res)
            else:
                left = mid + 1
        return res

    def _find_hour_by_speed(self, piles: List[int], k: int, h: int) -> bool:
        return sum(map(lambda x: math.ceil(x / k), piles)) <= h


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"piles": [3, 6, 7, 11], "h": 8}, "ans": 4},
        {"input": {"piles": [30, 11, 23, 4, 20], "h": 5}, "ans": 30},
        {"input": {"piles": [30, 11, 23, 4, 20], "h": 6}, "ans": 23},
        {"input": {"piles": [3], "h": 99}, "ans": 1},
        {"input": {"piles": [68], "h": 5}, "ans": 14},
    ]
    run(test_cases, s.minEatingSpeed)
