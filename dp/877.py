"""https://leetcode.com/problems/stone-game"""
from typing import List
from functools import lru_cache


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        r = len(piles) // 2
        l = r - 1
        alice, bob = 0, 0
        while r < len(piles):
            stones = max(piles[l], piles[r])
            alice += stones
            r += 1
            l -= 1
        bob = sum(piles) - alice
        return alice > bob

    def stoneGameDP(self, piles: List[int]) -> bool:
        """
        看不懂....
        """
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j:
                return 0
            parity = (j - i - N) % 2  # why?
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                return min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))

        return dp(0, N - 1) > 0
