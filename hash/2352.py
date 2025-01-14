"""https://leetcode.com/problems/equal-row-and-column-pairs/"""
from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        # tuple can act as hash key
        rm = Counter(tuple(el) for el in grid)
        # zip can transpose matrix
        for col in zip(*grid):
            # col is tuple
            count += rm[col]

        return count
