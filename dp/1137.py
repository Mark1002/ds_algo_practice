"""https://leetcode.com/problems/n-th-tribonacci-number."""


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dfs(n: int) -> int:
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            tri_num = dfs(n-1) + dfs(n-2) + dfs(n-3)
            memo[n] = tri_num
            return tri_num
        return dfs(n)
