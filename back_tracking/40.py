"""https://leetcode.com/problems/combination-sum-ii."""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: # noqa
        results = []
        candidates.sort()

        def backtracking(start: int, comb: List[int]):
            sum_comb = sum(comb)
            if sum_comb == target:
                results.append(comb[:])
                return
            if sum_comb > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                backtracking(i + 1, comb)
                comb.pop()

        backtracking(0, [])
        return results
