# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node):
            if not node:
                return 0

            right, left = maxDepth(node.right), maxDepth(node.left)

            if right == -1 or left == -1 or abs(right - left) > 1:
                return -1

            return 1 + max(right, left)
        return maxDepth(root) != -1 if root else True
