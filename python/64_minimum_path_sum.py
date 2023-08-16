import heapq
from typing import List


class Solution:

    # Bottom-Up Tabulation
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r < m - 1 and c < n - 1:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
                elif r < m - 1:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                elif c < n - 1:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                else:
                    dp[r][c] = grid[r][c]

        return dp[0][0]

    # Prim's MST
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited, minHeap = set(), [(grid[0][0], 0, 0)]

        while minHeap:
            dist, row, col = heapq.heappop(minHeap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == m - 1 and col == n - 1:
                return dist

            for direction in {(0, 1), (1, 0)}:
                new_row, new_col = row + direction[0], col + direction[1]

                if new_row in range(m) and new_col in range(n):
                    heapq.heappush(minHeap, (dist + grid[new_row][new_col], new_row, new_col))

        return 0
