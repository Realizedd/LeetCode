from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest_area = 0

        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(m) or c not in range(n) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                largest_area = max(largest_area, dfs(r, c))

        return largest_area
