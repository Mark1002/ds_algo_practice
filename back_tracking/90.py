"""https://leetcode.com/problems/subsets-ii"""
from typing import List
from utils import run


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        max_len = len(nums)

        def backtracking(cand: List[int], idx: int, hm: set):
            if tuple(sorted(cand)) not in hm:
                result.append(cand[:])
                hm.add(tuple(sorted(cand)))
            for i in range(idx, max_len):
                cand.append(nums[i])
                backtracking(cand, i+1, hm)
                cand.pop()
        backtracking([], 0, set())
        return result

    def netCodeSol(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(cand: List[int], idx: int):
            if idx == len(nums):
                res.append(cand[:])
                return
            # Add nums[idx]
            cand.append(nums[idx])
            backtracking(cand, idx+1)
            cand.pop()
            # skip dup element
            if idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            # Not add nums[idx]
            backtracking(cand, idx+1)

        backtracking([], 0)
        res.sort()
        return res


if __name__ == "__main__":
    s = Solution()
    test_cases = [{
        "input": {"nums": [1, 2, 2]},
        "ans": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    }]
    for func in [s.subsetsWithDup, s.netCodeSol]:
        run(test_cases, func)
