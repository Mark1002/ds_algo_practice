# https://leetcode.com/problems/determine-if-two-strings-are-close/
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        m1, m2 = Counter(word1), Counter(word2)
        s1 = {k for k in m1}
        s2 = {k for k in m2}
        a1 = sorted(m1.values())
        a2 = sorted(m2.values())
        return s1 == s2 and a1 == a2
