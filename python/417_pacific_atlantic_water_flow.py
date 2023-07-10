from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(prev, visit, r, c):
            if r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prev or (r, c) in visit:
                return

            dfs(heights[r][c], visit, r + 1, c)
            dfs(heights[r][c], visit, r, c + 1)
            dfs(heights[r][c], visit, r - 1, c)
            dfs(heights[r][c], visit, r, c - 1)

        for col in range(n):
            dfs(-1, pac, 0, col)
            dfs(-1, atl, m - 1, col)

        for row in range(m):
            dfs(-1, pac, row, 0)
            dfs(-1, atl, row, n - 1)

        for row in range(m):
            for col in range(n):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res


sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))