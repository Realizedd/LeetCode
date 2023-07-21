from collections import deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        graph = {start: deque() for start, dest in tickets}

        for start, dest in tickets:
            graph[start].append(dest)

        path = ['JFK']

        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True
            if node not in graph:
                return False

            for c in list(graph[node]):
                val = graph[node].popleft()
                path.append(val)

                if dfs(c):
                    return True

                path.pop()
                graph[node].append(val)

            return False

        dfs('JFK')
        return path


sol = Solution()
print(sol.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
