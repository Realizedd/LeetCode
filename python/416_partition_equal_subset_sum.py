from typing import List


class Solution:
    # Top-Down Memoization
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target //= 2
        dp = [[-1] * len(nums) for _ in range(target + 1)]

        def dfs(idx, cur):
            if cur == target:
                return 1
            if cur > target or idx >= len(nums):
                return 0
            if dp[cur][idx] != -1:
                return dp[cur][idx]

            res = dfs(idx + 1, cur) or dfs(idx + 1, cur + nums[idx])
            dp[cur][idx] = res
            return res

        return dfs(0, 0)

    # Bottom-Up Tabulation
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target //= 2
        dp = [[0] * (target + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = 1

        if target >= nums[0]:
            dp[0][nums[0]] = 1

        for idx in range(1, len(nums)):
            for cur in range(target + 1):
                dp[idx][cur] = dp[idx - 1][cur]

                if cur - nums[idx] >= 0:
                    dp[idx][cur] += dp[idx - 1][cur - nums[idx]]

        return dp[len(nums) - 1][target] > 0

    def canPartitionPowerSet(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target //= 2
        pset = set()
        pset.add(0)

        for n in nums:
            pset.update([x + n for x in pset])

        return target in pset
