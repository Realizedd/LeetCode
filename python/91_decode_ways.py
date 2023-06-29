class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1 if s[0] != '0' else 0

        if n == 1:
            return dp[0]

        if s[1] == '0' and (int(s[0] + s[1]) > 20 or int(s[0] + s[1]) <= 0):
            return 0

        dp[1] = dp[0] + (1 if s[0] != '0' and s[1] != '0' and 0 < int(s[0] + s[1]) < 27 else 0)

        for i in range(2, n):
            prev = s[i - 1]
            cur = s[i]

            if cur == '0' and (int(prev + cur) > 20 or int(prev + cur) <= 0):
                return 0

            if cur == '0':
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1] + (dp[i - 2] if prev != '0' and 0 < int(prev + cur) < 27 else 0)

        return dp[n - 1]


sol = Solution()
print(sol.numDecodings('2101'))
