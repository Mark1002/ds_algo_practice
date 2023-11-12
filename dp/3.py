"""
url: https://leetcode.com/problems/longest-substring-without-repeating-characters # noqa
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if d.get(s[r]) is not None:
                l = max(l, d[s[r]] + 1)
            d[s[r]] = r
            print(f"({l}, {r})")
            max_len = max(max_len, r-l+1)
        return max_len


if __name__ == "__main__":
    s = Solution()
    test_cases = ["abcabcbb", "bb", "pwwkew", "abba"]
    for test_case in test_cases:
        print(s.lengthOfLongestSubstring(test_case))
