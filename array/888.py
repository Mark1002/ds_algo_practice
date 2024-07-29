"""https://leetcode.com/problems/fair-candy-swap/."""
from typing import List
from utils import run


class Solution:
    def fairCandySwap(
        self, aliceSizes: List[int], bobSizes: List[int]
    ) -> List[int]:
        a_sum = sum(aliceSizes)
        b_sum = sum(bobSizes)
        half_sum = (a_sum + b_sum) // 2  # 相加除以二得出交換後的相等和
        b_m = set(bobSizes)

        for a_candy in aliceSizes:  # 只考慮一邊就好
            b_candy = half_sum - (a_sum - a_candy)  # 如此就可以推敲出交換的candy要為多少
            if b_candy in b_m:
                return [a_candy, b_candy]
        return []


if __name__ == "__main__":
    test_cases = [
        {
            "input": {
                "aliceSizes": [4, 1, 2, 1, 1, 2], "bobSizes": [3, 6, 3, 3]
            },
            "ans": [4, 6]
        },
        {
            "input": {"aliceSizes": [5, 7, 4, 6], "bobSizes": [1, 2, 3, 8]},
            "ans": [5, 1]
        }
    ]
    s = Solution()
    run(test_cases, s.fairCandySwap)
