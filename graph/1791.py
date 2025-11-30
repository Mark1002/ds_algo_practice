"""https://leetcode.com/problems/find-center-of-star-graph/."""
from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = defaultdict(int)

        for u, v in edges:
            degree[u]+=1
            degree[v]+=1
            if degree[u] > 1:
                return u
            if degree[v] > 1:
                return v
