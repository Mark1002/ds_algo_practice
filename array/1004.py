"""
1004. Max Consecutive Ones III
url: https://leetcode.com/problems/max-consecutive-ones-iii/
"""
from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        w_start, w_end = 0, 0
        A_len = len(A)
        for w_end in range(A_len):
            if A[w_end] == 0:
                K -= 1
            if K < 0:
                if A[w_start] == 0:
                    K += 1
                w_start += 1
        max_1_num = w_end - w_start + 1
        return max_1_num

def main():
    """Main."""
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    s = Solution()
    result = s.longestOnes(A, K)
    print(result)

if __name__ == "__main__":
    main()
