"""https://leetcode.com/problems/binary-tree-level-order-traversal"""
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        result = []
        result.append([root.val])
        q.append((root, 0))
        while q:
            node, lv = q.popleft()
            if not node:
                continue
            q.append((node.left, lv+1))
            q.append((node.right, lv+1))
            if node.left:
                if len(result)-1 < lv+1:
                    result.append([node.left.val])
                else:
                    result[lv+1].append(node.left.val)
            if node.right:
                if len(result)-1 < lv+1:
                    result.append([node.right.val])
                else:
                    result[lv+1].append(node.right.val)
        return result
