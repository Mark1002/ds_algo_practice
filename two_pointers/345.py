"""https://leetcode.com/problems/reverse-vowels-of-a-string"""


class Solution:

    def twoPointerReverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ss = list(s)
        l, r = 0, len(ss)-1
        while l < r:
            while ss[l] not in vowels and l < r:
                l += 1
            while ss[r] not in vowels and l < r:
                r -= 1
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1
        return "".join(ss)

    def OriginReverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        temp = []
        temp_2 = [None] * len(s)
        vo_idx = []
        for i in range(len(s)):
            char = s[i]
            if (char in vowels) or (chr(ord(char) + 32) in vowels):
                temp.append(char)
                vo_idx.append(i)
            else:
                temp_2[i] = char

        for i in vo_idx:
            temp_2[i] = temp.pop()

        return "".join(temp_2)
