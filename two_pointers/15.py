"""
https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = set()
        result = []
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    if (nums[i], nums[l], nums[r]) not in h:
                        result.append([nums[i], nums[l], nums[r]])
                        h.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        return result


if __name__ == "__main__":
    test_cases = [
        {"input": [-1, 0, 1, 2, -1, -4], "output": [[-1, -1, 2], [-1, 0, 1]]},
        {"input": [0, 1, 1], "output": []},
        {"input": [0, 0, 0], "output": [[0, 0, 0]]}
    ]
    for test_case in test_cases:
        s = Solution()
        result = s.threeSum(test_case["input"])
        expected = test_case["output"]
        if result != expected:
            raise AssertionError(f"want: {expected}, but get {result}")
