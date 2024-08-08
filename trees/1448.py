"""https://leetcode.com/problems/count-good-nodes-in-binary-tree"""
# Definition for a binary tree node.
from typing import Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = {"count": 1}

        def dfs(root: TreeNode, good: Dict[str, int], max_p: int):
            if root is None:
                return
            left = root.left
            right = root.right
            if left:
                left_max_p = max(max_p, left.val)
                if left.val >= max_p:
                    good["count"] += 1
                dfs(left, good, left_max_p)
            if right:
                right_max_p = max(max_p, right.val)
                if right.val >= max_p:
                    good["count"] += 1
                dfs(right, good, right_max_p)
        dfs(root, good, root.val)
        return good["count"]
