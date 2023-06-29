# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurMaxDepth(root)

    def recurMaxDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.recurMaxDepth(node.left), self.recurMaxDepth(node.right))
