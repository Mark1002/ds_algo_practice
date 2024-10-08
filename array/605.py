"""https://leetcode.com/problems/can-place-flowers."""
from typing import List
from utils import run


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_zero_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0) # noqa
                is_zero_left = (i == 0) or (flowerbed[i-1] == 0)
                if is_zero_left and is_zero_right:
                    count += 1
                    flowerbed[i] = 1
        return count >= n


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"flowerbed": [1, 0, 0, 0, 1], "n": 1}, "ans": True},
        {"input": {"flowerbed": [1, 0, 0, 0, 0, 1], "n": 2}, "ans": False},
        {"input": {"flowerbed": [0, 0, 1], "n": 1}, "ans": True}
    ]

    run(test_cases, s.canPlaceFlowers)
