"""https://leetcode.com/problems/kth-smallest-element-in-a-bst."""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.k_val = None

        def inorder(node):
            if node is None:
                return
            # left
            inorder(node.left)
            # root
            if self.k > 0:
                self.k -= 1
            if self.k == 0:
                if self.k_val is None:  # prevent k_val asign again
                    self.k_val = node.val
                    return
            else:
                # right
                inorder(node.right)

        inorder(root)
        return self.k_val
