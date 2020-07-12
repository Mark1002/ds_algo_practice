"""112 path sum
url: https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        paths = []
        self.collect_paths(root, 0, paths)
        return sum in paths
    
    def collect_paths(self, root: TreeNode, path_sum: int, paths: list):
        if root is None:
            return
        path_sum += root.val
        if root.left is None and root.right is None:
            paths.append(path_sum)
        self.collect_paths(root.left, path_sum, paths)
        self.collect_paths(root.right, path_sum, paths)
