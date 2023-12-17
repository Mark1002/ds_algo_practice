"""
https://leetcode.com/problems/min-stack/description/
"""
from typing import List, Dict


class MinStack:

    def __init__(self):
        self.stack: List[Dict[str, int]] = []
        self.cur_min = None

    def _check_valid(self):
        if len(self.stack) == 0:
            raise ValueError("stack is empty")

    def push(self, val: int) -> None:
        self.cur_min = val if self.cur_min is None else min(self.cur_min, val)
        self.stack.append({"value": val, "min": self.cur_min})

    def pop(self) -> None:
        self._check_valid()
        self.stack.pop()
        self.cur_min = self.getMin() if self.stack else None

    def top(self) -> int:
        self._check_valid()
        return self.stack[-1]["value"]

    def getMin(self) -> int:
        self._check_valid()
        return self.stack[-1]["min"]


if __name__ == "__main__":
    vals = [6, 7, 3, 2, -19, 22, 2]
    obj = MinStack()

    for val in vals:
        obj.push(val)

    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.push(3)
    print(obj.cur_min)
    print(obj.stack)
    print(obj.top(), obj.getMin())
