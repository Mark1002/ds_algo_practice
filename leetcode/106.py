"""106. Construct Binary Tree from Inorder and Postorder Traversal
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0 or len(postorder) == 0:
            return
        # get last element as root
        root_val = postorder[-1]
        root = TreeNode(val=root_val)
        # find root index in inorder
        root_index = inorder.index(root_val)
        # get left and right sub inorder
        in_lefts, in_rights = inorder[:root_index], inorder[root_index+1:]
        # get left and right sub postorder
        post_lefts, post_rights = postorder[:len(in_lefts)], postorder[len(in_lefts):-1]
        root.left = self.buildTree(in_lefts, post_lefts)
        root.right = self.buildTree(in_rights, post_rights)
        return root

def preorder_traveral(root):
    if root is None:
        return
    print(root.val)
    preorder_traveral(root.left)
    preorder_traveral(root.right)

def main():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]    
    s = Solution()
    root = s.buildTree(inorder, postorder)

    preorder_traveral(root)


if __name__ == "__main__":
    main()
