from typing import List


class Solution:
    def robList(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        first_max, last_max = self.robList(nums[1:]), self.robList(nums[:1])
        return max(first_max, last_max)
