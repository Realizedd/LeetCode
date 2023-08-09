from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        dp = {}

        def dfs(idx, p):
            if p == 0:
                return 0
            if idx >= len(nums) - 1:
                return float('inf')
            if (idx, p) in dp:
                return dp[(idx, p)]

            dp[(idx, p)] = min(max(dfs(idx + 2, p - 1), abs(nums[idx] - nums[idx + 1])), dfs(idx + 1, p))
            return dp[(idx, p)]

        return dfs(0, p)
