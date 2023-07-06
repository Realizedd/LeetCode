# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if not node:
                return 0
            res = 1 if node.val >= path_max else 0
            path_max = max(node.val, path_max)
            res += dfs(node.left, path_max)
            res += dfs(node.right, path_max)
            return res

        return dfs(root, root.val)
