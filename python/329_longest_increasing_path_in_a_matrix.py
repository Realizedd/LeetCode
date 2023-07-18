from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        calls = [0]

        def dfs(r, c, prev):
            if r not in range(m) or c not in range(n) or matrix[r][c] <= prev:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]

            calls[0] += 1
            num = matrix[r][c]
            dp[r][c] = 1 + max(dfs(r + 1, c, num), dfs(r - 1, c, num), dfs(r, c + 1, num), dfs(r, c - 1, num))
            return dp[r][c]

        longest = 0

        for row in range(m):
            for col in range(n):
                longest = max(longest, dfs(row, col, float('-inf')))

        print(calls)
        return longest


sol = Solution()
print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))