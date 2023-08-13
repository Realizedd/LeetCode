from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n

        def dfs(idx):
            if idx == n:
                return 1
            if idx == n - 1:
                return 0
            if dp[idx] != -1:
                return dp[idx]

            first = nums[idx]
            second = nums[idx + 1]
            res = first == second and dfs(idx + 2)

            if idx < n - 2:
                third = nums[idx + 2]
                res |= first == second and second == third and dfs(idx + 3)
                res |= first + 1 == second and second + 1 == third and dfs(idx + 3)

            dp[idx] = res
            return res

        return dfs(0)
