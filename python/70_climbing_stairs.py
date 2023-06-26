class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        return self.climbStairsRec(n, dp)

    def climbStairsRec(self, n, dp):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif dp[n]:
            return dp[n]

        dp[n] = self.climbStairsRec(n - 1, dp) + self.climbStairsRec(n - 2, dp)
        return dp[n]


sol = Solution()
print(sol.climbStairs(5))

