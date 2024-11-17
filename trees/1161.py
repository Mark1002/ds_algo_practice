"""https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        min_level = level = 0
        max_sum = float("-inf")
        q.append(root)

        while q:
            cur_level_sum = 0
            level += 1
            # len(q) is the same in the same iteration loop
            for _ in range(len(q)):
                node = q.popleft()
                # sum up same level value
                cur_level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                min_level = level
        return min_level
