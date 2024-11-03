"""https://leetcode.com/problems/word-break/"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if s[i:i+len(word)] != word:
                    continue
                if dfs(i+len(word)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)
