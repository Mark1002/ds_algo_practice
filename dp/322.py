import math
from typing import List
from utils import run


class Solution:
    def TopDownCoinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def find_coin(amount) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            if amount in mem:
                return mem[amount]
            min_coins = math.inf
            for coin in coins:
                remain = amount - coin
                result = find_coin(remain)
                if result != math.inf:
                    min_coins = min(min_coins, result + 1)
            mem[amount] = min_coins
            return min_coins

        min_coins = find_coin(amount)
        return min_coins if min_coins != math.inf else -1

    def BottomUpCoinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                remain = i - coin
                if remain >= 0:
                    dp[i] = min(dp[i], dp[remain]+1)
        return dp[amount] if dp[amount] != math.inf else -1


if __name__ == "__main__":
    s = Solution()
    run(
        [
            {"input": {"coins": [1], "amount": 0}, "ans": 0},
            {"input": {"coins": [1, 3, 4, 5], "amount": 7}, "ans": 2},
            {"input": {"coins": [1, 2], "amount": 3}, "ans": 2},
            {"input": {"coins": [2], "amount": 3}, "ans": -1}
        ],
        s.BottomUpCoinChange
    )
