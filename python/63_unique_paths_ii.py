from typing import List


class Solution:

    # Top-Down Memoization
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r == m - 1 and c == n - 1:
                return 1
            if r not in range(m) or c not in range(n) or obstacleGrid[r][c] == 1:
                return 0

            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)

    # Bottom-Up Tabulation
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            if obstacleGrid[r][0] == 1:
                break

            dp[r][0] = 1

        for c in range(n):
            if obstacleGrid[0][c] == 1:
                break

            dp[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]

