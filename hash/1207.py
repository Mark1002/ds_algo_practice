"""https://leetcode.com/problems/unique-number-of-occurrences/"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c_d = Counter(arr)
        seen = set()
        for k in c_d:
            if c_d[k] in seen:
                return False
            seen.add(c_d[k])
        return True
