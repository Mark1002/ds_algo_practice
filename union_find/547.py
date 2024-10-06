"""https://leetcode.com/problems/number-of-provinces."""
from typing import List
from utils import run


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.m = [i for i in range(n)]
        self.count = n

        def find(a: int) -> int:
            if self.m[a] == a:
                return a
            self.m[a] = find(self.m[a])
            return self.m[a]

        def union(a: int, b: int):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                # root_a as parent of root_b
                self.m[root_b] = root_a
                self.count -= 1

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j]:
                    union(i, j)

        return self.count


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {
                "isConnected": [
                    [1, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 1, 1],
                    [0, 0, 1, 1],
                ]
            },
            "ans": 2
        }
    ]
    run(test_cases, s.findCircleNum)
