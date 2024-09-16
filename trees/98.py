"""https://leetcode.com/problems/validate-binary-search-tree/"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal BST will be a ascend incremental sequence
        self.pre = None

        def inorder(root):
            if root is None:
                return True
            # left
            left_valid = inorder(root.left)
            # root
            if self.pre is not None and root.val <= self.pre.val:
                return False
            self.pre = root
            # right
            right_valid = inorder(root.right)
            return left_valid and right_valid
        return inorder(root)
