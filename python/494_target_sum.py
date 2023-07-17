from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def permutation(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx, total)] = permutation(idx + 1, total + nums[idx]) + permutation(idx + 1, total - nums[idx])
            return dp[(idx, total)]

        return permutation(0, 0)