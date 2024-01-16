"""
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List
from utils import run


# Need to study backtracking
class Solution:

    def gen_parenthesis(self, open: int, close: int):
        print(f"stack: {self.stack}, (open, close): {(open, close)}")
        if open == self.n == close:
            self.res.append("".join(self.stack))
            return

        if open < self.n:
            self.stack.append("(")
            self.gen_parenthesis(open+1, close)
            self.stack.pop()

        if close < open:
            self.stack.append(")")
            self.gen_parenthesis(open, close+1)
            self.stack.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.stack = []
        self.res = []
        self.n = n
        self.gen_parenthesis(0, 0)
        return self.res


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": 2,
            "ans": ["(())", "()()"],
        },
        # {
        #     "input": 3,
        #     "ans": ["((()))", "(()())", "(())()", "()(())", "()()()"]
        # },
    ]
    run(test_cases, s.generateParenthesis)
