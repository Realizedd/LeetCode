from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return True

        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)
