"""https://leetcode.com/problems/same-tree/."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = []
        s.append((p, q))
        while s:
            p, q = s.pop()
            if p is None and q is not None:
                return False
            if q is None and p is not None:
                return False
            if p is not None or q is not None:
                if p.val != q.val:
                    return False
                s.append((p.right, q.right))
                s.append((p.left, q.left))
        return True
