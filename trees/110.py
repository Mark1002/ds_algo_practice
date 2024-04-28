# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0

        def get_height(root: Optional[TreeNode]):
            if root is None:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)
            diff = left - right if left >= right else right - left
            self.diff = max(self.diff, diff)
            return max(left, right) + 1

        get_height(root)

        return self.diff < 2
