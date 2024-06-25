"""https://leetcode.com/problems/combination-sum/"""

from typing import List

from utils import run


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        max_len = len(candidates)

        def backtracking(start: int, comb: List[int]):
            comb_sum = sum(comb)
            if comb_sum == target:
                result.append(comb[:])
                return
            if comb_sum > target:
                return

            for i in range(start, max_len):
                comb.append(candidates[i])
                backtracking(i, comb)
                comb.pop()

        backtracking(0, [])
        return result


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {"candidates": [2, 3, 5], "target": 8},
            "ans": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

        }
    ]
    run(test_cases, s.combinationSum)
