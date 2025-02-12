"""https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left: bool, path: int) -> int:
            if node is None:
                return path
            # 從左邊走
            if is_left:
                path = max(
                    dfs(node.right, False, path+1),  # 下一段往右加一
                    dfs(node.left, True, 0)  # 從第二個左邊要歸零
                )
            # 從右邊走
            else:
                path = max(
                    dfs(node.left, True, path+1),  # 下一段往左加一
                    dfs(node.right, False, 0)  # 從第二個右邊要歸零
                )
            return path
        return max(dfs(root, True, -1), dfs(root, False, -1))
