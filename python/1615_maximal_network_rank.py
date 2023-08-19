from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {k: set() for k in range(n)}

        for start, end in roads:
            graph[start].add(end)
            graph[end].add(start)

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                if i == j:
                    continue

                rank = len(graph[i]) + len(graph[j])

                if j in graph[i]:
                    rank -= 1

                max_rank = max(max_rank, rank)

        return max_rank

