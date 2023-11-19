"""
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if not stack or d[stack.pop()] != c:
                    return False
        return False if stack else True


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": "]", "ans": False},
        {"input": ")", "ans": False},
        {"input": "()", "ans": True},
        {"input": "()[]{}", "ans": True},
        {"input": "(]", "ans": False},
        {"input": "{[]}", "ans": True},
    ]
    for test_case in test_cases:
        result = s.isValid(test_case["input"])
        expected = test_case["ans"]
        if result != expected:
            raise AssertionError(f"input: {test_case['input']}, want: {expected}, but get {result}") # noqa
