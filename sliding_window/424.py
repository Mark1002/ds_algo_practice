"""https://leetcode.com/problems/longest-repeating-character-replacement/
"""
from utils import run


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        d = {} # 紀錄char在w範圍內的出現次數
        max_sub_long = 0
        while r < len(s):
            c = s[r]
            d[c] = d.get(c, 0) + 1
            w = r - l + 1
            # w減去w範圍內出現最多的char次數，如果還遠大於k表示找不到更大的sub long
            if w - max(d.values()) > k:
                c = s[l]
                d[c] -= 1
                l += 1
            else:
                max_sub_long = max(max_sub_long, w)
            r += 1
        return max_sub_long


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": {"s": "ABAB", "k": 2}, "ans": 4},
        {"input": {"s": "ZGZSAASFHIUA", "k": 2}, "ans": 4},
    ]
    run(test_cases, s.characterReplacement)
