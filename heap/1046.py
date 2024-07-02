"""https://leetcode.com/problems/last-stone-weight/description/"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            temp = y - x
            if temp != 0:
                heapq.heappush(heap, temp)
        return -1*heap[0] if heap else 0
