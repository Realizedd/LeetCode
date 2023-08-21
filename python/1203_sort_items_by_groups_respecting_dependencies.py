from collections import defaultdict
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]

            while stack:
                cur = stack.pop()
                visited.append(cur)

                for c in graph[cur]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        stack.append(c)

            return visited if len(visited) == len(graph) else []

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        ordered_groups = defaultdict(list)

        for item in item_order:
            ordered_groups[group[item]].append(item)

        ans = []

        for group_index in group_order:
            ans += ordered_groups[group_index]

        return ans
