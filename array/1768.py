"""https://leetcode.com/problems/merge-strings-alternately."""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        more = ""
        w_l1, w_l2 = len(word1), len(word2)
        if w_l1 > w_l2:
            more = word1[w_l2:]
        elif w_l1 < w_l2:
            more = word2[w_l1:]

        for c1, c2 in zip(word1, word2):
            merge += c1 + c2
        return merge + more
