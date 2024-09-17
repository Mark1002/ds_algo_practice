"""https://leetcode.com/problems/validate-binary-search-tree/"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Inorder traversal BST will be a ascend incremental sequence.
    BST inorder traversal:
    1,2,3,4,5,6 (O) valid BST
    1,3,2,4,5,6 (X) invalid BST
    """
    def recur_isValidBST(self, root: Optional[TreeNode]) -> bool:
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

    def iterate_isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        pre = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if pre is not None and pre.val >= node.val:
                return False
            pre = node
            cur = node.right
        return True
