# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [root.val]

        def dfs(node):
            if not node:
                return 0

            val = node.val
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_sum[0] = max(max_sum[0], left + val + right)
            return val + max(left, right)

        dfs(root)
        return max_sum[0]
