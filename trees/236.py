"""https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree."""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        l_node = self.lowestCommonAncestor(root.left, p, q)
        r_node = self.lowestCommonAncestor(root.right, p, q)

        if l_node and r_node:
            return root
        # propagate 回傳不為空，在左子樹或右子樹找到的 p or q
        return l_node or r_node
