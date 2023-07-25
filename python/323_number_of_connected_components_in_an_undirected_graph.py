from collections import defaultdict
from typing import List


class Solution:
    # DFS
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True

            for c in graph[node]:
                dfs(c)

        res = 0

        for i in range(n):
            if visited[i]:
                continue

            res += 1
            dfs(i)

        return res

