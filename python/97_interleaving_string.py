class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(m, n):
            if m == len(s1) and n == len(s2):
                return True
            if dp[m][n] != -1:
                return dp[m][n]

            if m < len(s1) and s3[m + n] == s1[m] and dfs(m + 1, n):
                return True

            if n < len(s2) and s3[m + n] == s2[n] and dfs(m, n + 1):
                return True

            dp[m][n] = False
            return False

        return dfs(0, 0)
