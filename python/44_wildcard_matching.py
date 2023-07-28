class Solution:
    # Top-Down Memoization DP
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def match(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(p):
                return not s or i == len(s)

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '?')

            if first_match:
                dp[(i, j)] = match(i + 1, j + 1)
                return dp[(i, j)]
            elif p[j] == '*':
                dp[(i, j)] = i < len(s) and match(i + 1, j) or match(i, j + 1)
                return dp[(i, j)]

            return False

        return match(0, 0)

    # Bottom-Up Tabulation DP
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # Edge Case of empty string matched with a pattern
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break

            dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                first_match = i - 1 < len(s) and (s[i - 1] == p[j - 1] or p[j - 1] == '?')

                if first_match:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = i - 1 < len(s) and dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        return dp[len(s)][len(p)]
