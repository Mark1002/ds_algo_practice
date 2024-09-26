"""https://leetcode.com/problems/kth-largest-element-in-an-array/"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Only get the first k elements
        min_heap = nums[:k]
        # Assume the first(smallest) element is kth largest element
        heapq.heapify(min_heap)

        for num in nums[k:]:
            # if the other n-k elements larger than kth largest element
            # it means that k+1th~nth largest elements can't all happen here
            if num > min_heap[0]:
                # maintain kth largest element at first position
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]

    def SlowerSolution(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = n - k + 1  # nth largest is equal n-k-1 th smallest
        heapq.heapify(nums)
        while s > 0:
            result = heapq.heappop(nums)
            s -= 1
        return result
