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
        """My solution."""
        p_path = []
        q_path = []

        def dfs(node, target, root_path):
            root_path.append(node)
            if target is node:
                return
            if target.val > node.val:
                dfs(node.right, target, root_path)
            else:
                dfs(node.left, target, root_path)
        dfs(root, p, p_path)
        dfs(root, q, q_path)
        low_ances = None
        for p_a, q_a in zip(p_path, q_path):
            if p_a is q_a:
                low_ances = p_a
        return low_ances

    def betterSolution(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        """利用 binart search tree 的特性，(p, q) 在同一個
        subtree 必定小於或是大於 root。反之，就是共同的最小 root
        """
        while root:
            if p.val > root.val < q.val:
                root = root.right
            elif p.val < root.val > q.val:
                root = root.left
            else:
                return root
