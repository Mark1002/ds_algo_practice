"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""
from typing import List
from utils import run


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                right, left = stack.pop(), stack.pop()
                stack.append(int(eval(f"{left}{token}{right}")))
            else:
                stack.append(token)
        return int(stack.pop())


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": ["18"], "ans": 18},
        {"input": ["2", "1", "+", "3", "*"], "ans": 9},
        {"input": ["4", "13", "5", "/", "+"], "ans": 6},
        {"input": ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], "ans": 22}, # noqa
        {"input": ["-2", "3", "/"], "ans": 0},
    ]
    run(test_cases, s.evalRPN)
