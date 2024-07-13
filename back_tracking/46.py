"""https://leetcode.com/problems/permutations/."""
from typing import List
from utils import run


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def perm(cond: List[int], hm: set):
            if len(cond) == len(nums):
                result.append(cond[:])
                return
            for num in nums:
                if num not in hm:
                    cond.append(num)
                    hm.add(num)
                    perm(cond, hm)
                    cond.pop()
                    hm.remove(num)
        perm([], set())
        return result


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {"nums": [1, 2, 3]},
            "ans": [
                [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1] # noqa
            ]
        }
    ]
    run(test_cases, s.permute)
