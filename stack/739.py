"""
https://leetcode.com/problems/daily-temperatures/description/
https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/
"""
from typing import List, Tuple
from utils import run


class Solution:
    def BruteForceDailyTemperatures(
        self, temperatures: List[int]
    ) -> List[int]:
        t_len = len(temperatures)
        ans = [0] * t_len
        for i in range(t_len):
            s = []
            for j in range(i+1, t_len):
                s.append(temperatures[j])
                if temperatures[j] > temperatures[i]:
                    ans[i] = len(s)
                    break
        return ans

    def MonotonicStackDailyTemperatures(
        self, temperatures: List[int]
    ) -> List[int]:
        ans = [0] * len(temperatures)
        s: List[Tuple[int, int]] = []
        for i, t in enumerate(temperatures):
            while s and s[-1][1] < t:
                j, _ = s.pop()
                ans[j] = i - j
            s.append((i, t))
        return ans


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {"temperatures": [73, 74, 75, 71, 69, 72, 76, 73]},
            "ans": [1, 1, 4, 2, 1, 1, 0, 0]
        }
    ]
    run(test_cases, s.MonotonicStackDailyTemperatures)
