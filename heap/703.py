"""https://leetcode.com/problems/kth-largest-element-in-a-stream"""
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # 利用最小堆積反過來達到第k大的 element
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
