"""
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = max(w * h, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return area


if __name__ == "__main__":
    test_cases = [
        {"input": [1, 8, 6, 2, 5, 4, 8, 3, 7], "output": 49},
        {"input": [1, 1], "output": 1},
        {"input": [0, 0], "output": 0},
    ]

    for test_case in test_cases:
        s = Solution()
        result = s.maxArea(test_case["input"])
        expected = test_case["output"]
        if result != expected:
            raise AssertionError(f"want: {expected}, but get {result}")
