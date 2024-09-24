"""https://leetcode.com/problems/time-based-key-value-store"""
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        records = self.m[key]
        left, right = 0, len(records)-1

        while left <= right:
            mid = (left + right) // 2
            if records[mid][1] == timestamp:
                return records[mid][0]
            if records[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if 0 <= right <= len(records)-1:
            return self.m[key][right][0]
        else:
            return ""
