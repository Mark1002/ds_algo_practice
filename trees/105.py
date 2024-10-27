"""https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal""" # noqa
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == len(inorder) == 0:
            return None
        # preorder 決定 root
        root = TreeNode(preorder[0])
        if len(preorder) == len(inorder) == 1:
            return root
        # inorder 決定 left and right
        i = inorder.index(preorder[0])
        in_left, in_right = inorder[:i], inorder[i+1:]
        j = len(in_left)
        pre_left, pre_right = preorder[1:1+j], preorder[j+1:]

        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root
