# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            count = len(queue)

            for i in range(count):
                node = queue.popleft()

                if len(res) <= level:
                    res.append(node)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

            level += 1
        return res
