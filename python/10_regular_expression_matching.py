class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(2, len(p)):
            dp[0][j] = p[j] == '*' and dp[0][j - 2]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] != '*':
                    dp[i + 1][j + 1] = dp[i][j] and (s[i] == p[j] or p[j] == '.')
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

                    if s[i] == p[j - 1] or p[j - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i][j + 1]

        return dp[-1][-1]


sol = Solution()
print(sol.isMatch('amazing', "a*maz.n*g"))
