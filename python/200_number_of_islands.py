from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for c in range(m):
                cur = grid[r][c]

                if cur == '1':
                    islands += 1
                    self.submerge(grid, n, m, r, c)

        return islands

    def submerge(self, grid, n, m, r, c):
        if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        self.submerge(grid, n, m, r + 1, c)
        self.submerge(grid, n, m, r, c + 1)
        self.submerge(grid, n, m, r - 1, c)
        self.submerge(grid, n, m, r, c - 1)


sol = Solution()
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))