
"""https://leetcode.com/problems/asteroid-collision."""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for stone in asteroids:
            # only [right, left] will collision
            while len(stack) > 0 and stone < 0 < stack[-1]:
                if stack[-1] > -stone:
                    break
                if stack[-1] == -stone:
                    stack.pop()
                    break
                if stack[-1] < -stone:
                    stack.pop()
            else:
                stack.append(stone)
        return stack
