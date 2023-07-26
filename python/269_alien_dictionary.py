from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = defaultdict(int)

        for i in range(1, len(words)):
            cur, prev = words[i], words[i - 1]
            minLen = min(len(prev), len(cur))

            if len(prev) > len(cur) and cur[:minLen] == prev[:minLen]:
                return ""

            for j in range(minLen):
                if cur[j] != prev[j]:
                    if cur[j] not in graph[prev[j]]:
                        indegree[cur[j]] += 1
                        graph[prev[j]].add(cur[j])

                    break

        zero_indegrees = deque([k for k in graph if k not in indegree])
        res = ''

        while zero_indegrees:
            vertex = zero_indegrees.popleft()
            res += vertex

            if vertex in graph:
                for neighbor in graph[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        zero_indegrees.append(neighbor)

        return res if len(res) == len(graph) else ''