class Solution:

    # Top-Down Memoization
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        def climb(i):
            if i < 0:
                return 0
            elif i == 0:
                return 1
            elif dp[i]:
                return dp[i]

            dp[i] = climb(i - 1) + climb(i - 2)
            return dp[i]

        return climb(n)

    # Bottom-Up Tabulation
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


sol = Solution()
print(sol.climbStairs(5))

