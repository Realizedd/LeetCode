# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        vertex_map = {node: Node(node.val)}
        stack = [node]

        while stack:
            n = stack.pop(0)

            if n not in vertex_map:
                vertex_map[n] = Node(n.val)

            for c in n.neighbors:
                if c not in vertex_map:
                    stack.append(c)
                    vertex_map[c] = Node(c.val)

                vertex_map[n].neighbors.append(vertex_map[c])

        return vertex_map[node] if node else None
