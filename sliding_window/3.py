"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from utils import run


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        h = {}
        left, right = 0, 0
        while right < len(s):
            if s[right] in h:
                left = max(h[s[right]] + 1, left)
            count = max(right - left + 1, count)
            h[s[right]] = right
            right += 1
        return count


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"s": "abcabcbb"}, "ans": 3},
        {"input": {"s": "bbbbb"}, "ans": 1},
        {"input": {"s": "pwwkew"}, "ans": 3},
        {"input": {"s": "pwwkew123456789kop"}, "ans": 14},
    ]
    run(test_cases, s.lengthOfLongestSubstring)
