import heapq
from typing import List


class Solution:
    # Dijkstra
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            val, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == m - 1 and c == n - 1:
                return val

            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]

                if nr in range(m) and nc in range(n) and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(val, grid[nr][nc]), nr, nc))

        return -1

    # DFS
    def swimInWaterDFS(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, curMax):
            if r not in range(m) or c not in range(n) or (r, c) in visited:
                return float('inf')

            curMax = max(grid[r][c], curMax)

            if r == m - 1 and c == n - 1:
                return curMax

            visited.add((r, c))
            res = min(dfs(r + 1, c, curMax),
                      dfs(r - 1, c, curMax),
                      dfs(r, c + 1, curMax),
                      dfs(r, c - 1, curMax))
            visited.remove((r, c))
            return res

        return dfs(0, 0, grid[0][0])


sol = Solution()
print(sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
))