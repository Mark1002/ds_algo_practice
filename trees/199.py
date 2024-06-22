# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def height(root) -> int:
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))
        h = height(root)
        if h == 0:
            return []
        result = h * [0]

        queue = deque()
        queue.append((root, 0))
        while queue:
            el, level = queue.popleft()
            result[level] = el.val
            level += 1
            if el.left:
                queue.append((el.left, level))
            if el.right:
                queue.append((el.right, level))
        return result
