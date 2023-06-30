# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = [0]

        def maxDepth(node):
            if not node:
                return 0

            left, right = maxDepth(node.left), maxDepth(node.right)
            depth[0] = max(depth[0], left + right)
            return 1 + max(left, right)

        maxDepth(root)
        return depth[0]