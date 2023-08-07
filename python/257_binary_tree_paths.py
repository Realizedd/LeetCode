# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(cur, ls):
            if not cur:
                return

            ls.append(str(cur.val))

            if not cur.left and not cur.right:
                ans.append('->'.join(ls))
            else:
                dfs(cur.left, ls)
                dfs(cur.right, ls)

            ls.pop()

        dfs(root, [])
        return ans
