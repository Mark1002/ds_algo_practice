"""https://leetcode.com/problems/k-closest-points-to-origin"""
import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for i, p in enumerate(points):
            x, y = p
            dis = math.sqrt(x**2+y**2)
            heap.append((dis, i))
        # O(n)
        heapq.heapify(heap)
        j = 0
        while j < k:
            _, i = heapq.heappop(heap)
            result.append(points[i])
            j += 1
        return result
