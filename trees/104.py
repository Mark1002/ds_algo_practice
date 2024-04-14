"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class IterateDFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth, max_depth = 0, 0
        if root is None:
            return max_depth
        stack.append((root, depth+1))
        while stack:
            cur, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if cur.right:
                stack.append((cur.right, depth+1))
            if cur.left:
                stack.append((cur.left, depth+1))
        return max_depth
