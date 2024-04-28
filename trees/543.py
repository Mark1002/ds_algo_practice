"""https://leetcode.com/problems/diameter-of-binary-tree/"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def max_height(root: Optional[TreeNode]) -> int:
            # one node diameter 為 0 調整樹高從-1開始
            if root is None:
                return -1
            left_h = max_height(root.left)
            right_h = max_height(root.right)
            # 觀察法diameter等於左右子樹高加上2邊
            self.diameter = max(left_h + right_h + 2, self.diameter)
            return max(left_h, right_h) + 1
        max_height(root)
        return self.diameter
