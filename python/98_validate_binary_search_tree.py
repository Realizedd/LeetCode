# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsMinMax(node, cur_min, cur_max):
            if not node:
                return True
            if node.val >= cur_max or node.val <= cur_min:
                return False

            return dfsMinMax(node.left, cur_min, node.val) and dfsMinMax(node.right, node.val, cur_max)

        return dfsMinMax(root, float('-inf'), float('inf'))
