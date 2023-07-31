class Solution:
    # Top-Down Memoization DP
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == m and j == n:
                return 0

            if i < m and j < n and s1[i] == s2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = float('inf')

                if i < m:
                    res = min(res, dfs(i + 1, j) + ord(s1[i]))

                if j < n:
                    res = min(res, dfs(i, j + 1) + ord(s2[j]))

                dp[(i, j)] = res

            return dp[(i, j)]

        return dfs(0, 0)


sol = Solution()
print(sol.minimumDeleteSum('delete', 'leet'))
