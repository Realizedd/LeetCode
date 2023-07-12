from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {idx: [] for idx in range(1, len(edges) + 1)}

        def dfs(idx, target):
            if idx in visited:
                return False

            visited.add(idx)

            if idx == target:
                return True

            return any(dfs(c, target) for c in adj[idx])

        for edge in edges:
            visited = set()

            if dfs(edge[0], edge[1]):
                return edge

            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

