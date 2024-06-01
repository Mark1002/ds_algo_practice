"""https://leetcode.com/problems/permutation-in-string/"""
from collections import Counter
from utils import run


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1

            # sliding window
            if i >= w and s2[i-w] in cntr:
                # recover value by step
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]):  # see optimized code below
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    test_cases = [{"input": {"s1": "abc", "s2": "ccccbbbbaaaa"}, "ans": False}]
    run(test_cases, s.checkInclusion)
