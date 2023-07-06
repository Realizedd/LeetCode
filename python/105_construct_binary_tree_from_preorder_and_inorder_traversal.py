# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeOptimized(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_idx])
        root.left = self.buildTree(preorder, inorder[0:root_idx])
        root.right = self.buildTree(preorder, inorder[(root_idx + 1):])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        inorder_left, inorder_right = inorder[0:root_idx], inorder[(root_idx + 1):len(inorder)]
        preorder_left, preorder_right = preorder[1:(1 + len(inorder_left))], preorder[(1 + len(inorder_left)):]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
