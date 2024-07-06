"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""
from typing import List
from utils import run


class Solution:
    """解題思路為將 rotate 的 array 先分為左右排序好的兩部分。
    左右部分中分別一樣優先寫出正常的 bin search 邏輯條件 (比較好寫)，
    反過來就是 rotate 部分的條件。
    """
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # left part
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # right part
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return l if nums[l] == target else -1


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, "ans": 4},
        {"input": {"nums": [1, 3], "target": 3}, "ans": 1},
        {"input": {"nums": [3, 1], "target": 1}, "ans": 1},
    ]
    run(test_cases, s.search)
