"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from utils import run


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        h = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in h:
                h.remove(s[left])
                left += 1
            h.add(s[right])
            count = max(right - left + 1, count)
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
