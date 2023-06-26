from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [0] * (n + 1)
        return self.minCostClimbingStairsRec(cost, n, dp)

    def minCostClimbingStairsRec(self, cost, index, dp):
        if index <= 1:
            return cost[index]
        elif dp[index]:
            return dp[index]

        dp[index] = cost[index] + min(self.minCostClimbingStairsRec(cost, index - 1, dp),
                                      self.minCostClimbingStairsRec(cost, index - 2, dp))
        return dp[index]


sol = Solution()
print(sol.minCostClimbingStairs([10,9]))
