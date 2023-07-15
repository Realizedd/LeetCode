from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target //= 2
        dp = [[-1] * len(nums) for _ in range(target)]

        def dfs(idx, cur):
            if cur == target:
                return 1
            if cur > target or idx >= len(nums):
                return 0
            if dp[idx][cur] != -1:
                return dp[idx][cur]

            res = dfs(idx + 1, cur) or dfs(idx + 1, cur + nums[idx])
            dp[idx][cur] = res
            return res

        return dfs(0, 0)

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
