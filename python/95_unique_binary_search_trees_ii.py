
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in dp:
                return dp[(start, end)]

            possible = []

            for i in range(start, end + 1):
                left, right = generate(start, i - 1), generate(i + 1, end)

                for l in left:
                    for r in right:
                        possible.append(TreeNode(i, l, r))

            dp[(start, end)] = possible
            return possible

        return generate(1, n)
