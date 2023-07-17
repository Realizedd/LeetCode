from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(rem, idx):
            if rem == 0:
                return 1
            if idx >= len(coins):
                return 0
            if dp[idx][rem] != -1:
                return dp[idx][rem]

            coin = coins[idx]

            if rem >= coin:
                dp[idx][rem] = dfs(rem - coin, idx) + dfs(rem, idx + 1)
            else:
                dp[idx][rem] = dfs(rem, idx + 1)

            return dp[idx][rem]

        return dfs(amount, 0)

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for c in range(n):
            dp[c][0] = 1

        for c in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[c][a] = dp[c + 1][a] + (dp[c][a - coins[c]] if a >= coins[c] else 0)

        return dp[0][amount]
