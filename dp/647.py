"""https://leetcode.com/problems/palindromic-substrings/."""


class Solution:
    def countSubstrings(self, s: str) -> int:
        pa_count = 0
        for i in range(len(s)):
            # odd palindromic ex: aba
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pa_count += 1
                l -= 1
                r += 1
            # even palindromic ex: bb
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pa_count += 1
                l -= 1
                r += 1
        return pa_count
