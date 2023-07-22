import heapq
from typing import List


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        res = 0

        while len(visited) < n:
            cost, cur = heapq.heappop(minHeap)

            if cur in visited:
                continue

            visited.add(cur)
            res += cost

            for i in range(n):
                heapq.heappush(minHeap, (manhattan(points[cur], points[i]), i))

        return res


sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))