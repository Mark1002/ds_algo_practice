"""https://leetcode.com/problems/maximum-subsequence-score."""
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_lists = sorted(zip(nums2, nums1), reverse=True)
        score = 0
        min_heap = []
        num1_sum = 0
        # num2 is the minimum at the current iteration
        for num2, num1 in sorted_lists:
            heapq.heappush(min_heap, num1)
            num1_sum += num1
            # maintain min heap of size k
            if len(min_heap) > k:
                el = heapq.heappop(min_heap)
                num1_sum -= el
            if len(min_heap) == k:
                # record the maximum score
                score = max(num2 * num1_sum, score)
        return score
