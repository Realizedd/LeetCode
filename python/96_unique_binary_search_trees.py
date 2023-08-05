class Solution:
    def numTrees(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def count(k):
            if k <= 1:
                return 1
            if dp[k] != -1:
                return dp[k]

            dp[k] = sum((count(i - 1) * count(k - i)) for i in range(1, k + 1))
            return dp[k]

        return count(n)
