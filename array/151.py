"""https://leetcode.com/problems/reverse-words-in-a-string."""


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        a = s.split(" ")
        for i in range(len(a)-1, -1, -1):
            if a[i] == "":
                continue
            result += a[i]
            if i > 0:
                result += " "
        return str.rstrip(result)
