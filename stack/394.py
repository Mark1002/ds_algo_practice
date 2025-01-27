"""https://leetcode.com/problems/decode-string."""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                decode = ""
                while stack[-1] != "[":
                    decode = stack.pop() + decode
                else:
                    # remove [
                    stack.pop()
                    # find multi num
                    mul = ""
                    while len(stack) > 0 and stack[-1] in nums:
                        mul = stack.pop() + mul
                    stack.append(int(mul) * decode)
        return "".join(stack)
