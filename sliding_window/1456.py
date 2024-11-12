"""https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = count = l = r = 0
        m = {"a", "e", "i", "o", "u"}
        while r < len(s):
            if s[r] in m:
                count += 1
            if r-l == k-1:
                max_vowel = max(max_vowel, count)
                if s[l] in m:
                    count -= 1
                l += 1
            r += 1
        return max_vowel
