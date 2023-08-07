# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(cur, total):
            if not cur:
                return False
            if not cur.left and not cur.right:
                return (total + cur.val) == targetSum
            return pathSum(cur.left, total + cur.val) | pathSum(cur.right, total + cur.val)

        return pathSum(root, 0)
