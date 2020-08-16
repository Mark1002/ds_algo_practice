"""
485. Max Consecutive Ones
url: https://leetcode.com/problems/max-consecutive-ones/
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = cur_count = 0
        for num in nums:
            if num == 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count = 0
        return max_count

def main():
    """Main."""
    nums = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    s = Solution()
    result = s.findMaxConsecutiveOnes(nums)
    print(result)

if __name__ == "__main__":
    main()
