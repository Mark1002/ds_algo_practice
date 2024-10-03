"""https://leetcode.com/problems/greatest-common-divisor-of-strings."""


class Solution:
    def PrefixGcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        short = min(str1, str2)
        for i in range(len(short)):
            prefix = short[:i+1]
            mul1 = len(str1) // len(prefix)
            mul2 = len(str2) // len(prefix)
            if (prefix * mul1 == str1) and (prefix * mul2 == str2):
                result = max(prefix, result)
        return result

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a % b)
        if str1 + str2 != str2 + str1:
            return ""

        gcd = GCD(len(str1), len(str2))
        return str1[:gcd]
