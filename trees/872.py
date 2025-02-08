"""https://leetcode.com/problems/leaf-similar-trees."""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar_recursive(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        leaf1, leaf2 = [], []

        def postorder(root, leaf):
            if root is None:
                return
            postorder(root.left, leaf)
            postorder(root.right, leaf)
            if root.left or root.right:
                return
            leaf.append(root.val)

        postorder(root1, leaf1)
        postorder(root2, leaf2)
        return leaf1 == leaf2

    def leafSimilar_iterate(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def postorder(root, leaf):
            stack = []
            stack.append(root)
            seen = set()
            while stack:
                cur = stack[-1]
                seen.add(cur)
                if cur.left in seen or cur.right in seen:
                    stack.pop()
                    continue
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                if cur.left is None and cur.right is None:
                    leaf.append(stack.pop().val)
        leaf1, leaf2 = [], []
        postorder(root1, leaf1)
        postorder(root2, leaf2)
        return leaf1 == leaf2
