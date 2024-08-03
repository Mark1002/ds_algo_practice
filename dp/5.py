"""https://leetcode.com/problems/longest-palindromic-substring/"""
from utils import run


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_helper(l: int, r: int, long_pa: str) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_pa = s[l:r+1]
                if len(cur_pa) > len(long_pa):
                    long_pa = cur_pa
                l -= 1
                r += 1
            return long_pa
        long_pa = s[0]
        for i in range(len(s)):
            # check odd palindrome
            l = r = i
            long_pa = longest_helper(l, r, long_pa)
            # check even palindrome
            l, r = i, i+1
            long_pa = longest_helper(l, r, long_pa)
        return long_pa


if __name__ == "__main__":
    s = Solution()
    test_cases = [{"input": {"s": "ccc"}, "ans": "ccc"}]
    run(test_cases, s.longestPalindrome)
