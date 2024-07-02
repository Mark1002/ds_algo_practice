"""https://leetcode.com/problems/subtree-of-another-tree/"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        def checkSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            """preorder check same."""
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val != subRoot.val:
                return False
            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)

        def dfs(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            """preorder travel all node."""
            if root is None:
                return False
            if checkSame(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

    def isSubtreeMyself(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        def fetchSameRoot(root):
            """Preorder to collect same root."""
            if root is None:
                return
            if root.val == subRoot.val:
                same_roots.append(root)
            fetchSameRoot(root.left)
            fetchSameRoot(root.right)

        def checkSame(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val != subRoot.val:
                return False
            return checkSame(root.left, subRoot.left) and checkSame(root.right, subRoot.right)

        same_roots = []
        fetchSameRoot(root)
        for root in same_roots:
            if checkSame(root, subRoot):
                return True
        return False
