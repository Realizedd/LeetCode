from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur_min = prices[0]
        profit = 0

        for i in range(1, n):
            v = prices[i]
            profit = max(profit, v - cur_min)

            if v < cur_min:
                cur_min = v

        return profit
