import heapq
from typing import List


class Solution:
    # Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {x: [] for x in range(1, n + 1)}

        for start, end, time in times:
            graph[start].append((time, end))

        visited = set()
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            time, idx = heapq.heappop(minHeap)

            if idx in visited:
                continue

            visited.add(idx)
            t = time

            for ntime, end in graph[idx]:
                if end not in visited:
                    heapq.heappush(minHeap, (time + ntime, end))

        return t if len(visited) == n else -1

    # DFS
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {x: [] for x in range(1, n + 1)}

        for start, end, time in times:
            graph[start].append((time, end))

        visited = set()
        times: List[int] = [-1] * n
        times[k - 1] = 0

        def dfs(cur, dist):
            if 0 < times[cur - 1] < dist:
                return

            times[cur - 1] = dist if times[cur - 1] == -1 else min(times[cur - 1], dist)

            visited.add(cur)

            for time, end in graph[cur]:
                if end not in visited:
                    dfs(end, dist + time)

            visited.remove(cur)

        dfs(k, 0)
        ans = times[0]

        for t in times:
            if t == -1:
                return -1

            ans = max(t, ans)

        return ans


sol = Solution()
print(sol.networkDelayTime([[1, 2, 1]], 2, 2))