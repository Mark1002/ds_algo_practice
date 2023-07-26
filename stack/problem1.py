"""
A string S consisting of the letters A, e, c and is given.
The string can be transformed either by removing a letter together with
an adjacent letters, or by removing a letter c together with an adjacent
letter 0.
Write a function:
that given a string S consisting of N characters, returns any string that:
• can be obtained from S by repeatedly applying the described transformation,
and cannot be further transformed.
If at some point there is more than one possible way to transform the string,
any of the valid transformations may be chosen.
Examples:
1. Given S = "CBACD", the function may return 'C', because one of the possible
sequences of operations is as follows:
CBACD -> CBA -> C
2. Given S = "CABABD" the function may return an empty string, because one
possible sequence of operations is:
CABABD  -> CABD -> CD ->
"""


def solution(S):
    stack = []
    for char in S:
        if len(stack) > 0:
            top = stack[-1]
            if (top == "B" and char == "A") or (top == "A" and char == "B"):
                stack.pop()
                continue
            elif (top == "C" and char == "D") or (top == "D" and char == "C"):
                stack.pop()
                continue
        stack.append(char)
    return "".join(stack)


if __name__ == "__main__":
    test_cases = ["CBACD", "CABABD", "ACBDACBD"]
    for test_case in test_cases:
        print(f"{test_case} => {solution(test_case)}")
