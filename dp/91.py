"""https://leetcode.com/problems/decode-ways/."""


class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string is empty or starts with '0', it cannot be decoded
        if s[0] == "0":
            return 0
        n = len(s)
        # dp[i] represents the number of ways to decode the substring s[:i]
        dp = [0] * (n+1)
        # Base cases
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode a string of length 1, assuming it's not '0'
        for i in range(2, n+1):
            # Single digit decode, if valid (i.e., 1-9)
            one_digit = s[i-1:i]
            if one_digit != "0":
                dp[i] += dp[i-1]
            # Two digit decode, if valid (i.e., 10-26)
            two_digit = s[i-2:i]
            if 10 <= int(two_digit) <= 26:
                dp[i] += dp[i-2]
        return dp[n]
