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

    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            i, cnt = 0, 0

            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1

                if cnt == p:
                    return True

            return False

        if p == 0:
            return 0

        nums.sort()
        l, r = 0, 10 ** 9
        res = 10 ** 9

        while l <= r:
            m = l + (r - l) // 2

            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
