"""https://leetcode.com/problems/subsets/"""

from typing import List

from utils import run


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        max_len = len(nums)

        def backtracking(start_idx: int, a: List[int], result: List[List[int]]):
            for i in range(start_idx, max_len):
                cur_idx, end_idx = i, i+1
                print(end_idx)
                a = a + nums[cur_idx:end_idx]
                print(f"a: {a}")
                result.append(a.copy())
                backtracking(end_idx, a, result)
                a.pop()
        backtracking(0, [], result)
        return result


if __name__ == "__main__":
    s = Solution()
    test_cases = [{"input": {"nums": [2, 6]}, "ans": [[], [2], [6], [2, 6]]}]
    run(test_cases, s.subsets)
