"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return [left+1, right+1]


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"numbers": [2, 7, 11, 15], "target": 9}, "ans": [1, 2]},
        {"input": {"numbers": [-1, 0], "target": -1}, "ans": [1, 2]},
        {"input": {"numbers": [2, 3, 4], "target": 6}, "ans": [1, 3]},
    ]
    for test_case in test_cases:
        result = s.twoSum(**test_case["input"])
        expected = test_case["ans"]
        if result != expected:
            raise AssertionError(f"want: {expected}, but get {result}")
