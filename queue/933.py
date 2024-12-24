"""https://leetcode.com/problems/number-of-recent-calls."""
from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        start = t - 3000
        self.q.append(t)
        while self.q[0] < start:
            self.q.popleft()
        return len(self.q)
