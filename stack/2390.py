"""https://leetcode.com/problems/removing-stars-from-a-string."""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 0 and c == "*" and stack[-1] != "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
