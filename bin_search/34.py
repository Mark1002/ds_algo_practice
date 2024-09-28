"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array""" # noqa
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        if right < left:
            return [-1, -1]
        # find first
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid-1  # Search on the left side
            else:
                left = mid+1
        first = left
        if first < 0 or first >= len(nums) or nums[first] != target:
            return [-1, -1]
        # find last
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid+1  # Search on the right side
            else:
                right = mid-1
        last = right
        if last < 0 or last >= len(nums) or nums[last] != target:
            return [-1, -1]
        return [first, last]

    def BetterSolution(self, nums: List[int], target: int) -> List[int]:
        # By chatGPT
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid  # keep track of the found index
                    right = mid - 1  # search on the left side for the first occurrence # noqa
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid  # keep track of the found index
                    left = mid + 1  # search on the right side for the last occurrence # noqa
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        # Find first and last positions
        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]
