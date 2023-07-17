from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[''] * len(prices) for _ in range(2)]

        def dfs(buy, idx):
            if idx >= len(prices):
                return 0
            if dp[buy][idx]:
                return dp[buy][idx]

            buyOrSell, hold = 0, dfs(buy, idx + 1)

            if buy:
                buyOrSell = -prices[idx] + dfs(0, idx + 1)
            else:
                buyOrSell = prices[idx] + dfs(1, idx + 2)

            dp[buy][idx] = max(buyOrSell, hold)
            return dp[buy][idx]

        return dfs(1, 0)


sol = Solution()
print(sol.maxProfit([22,5,1,6,12,5,2,5,8,4,7,4,8,2,6,1,5,30]))
