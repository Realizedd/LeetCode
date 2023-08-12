from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_num = nums[0]

        for n in nums:
            counter[n] += n
            max_num = max(max_num, n)

        dp = {}

        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return counter[1]
            if i in dp:
                return dp[i]

            dp[i] = max(dfs(i - 1), dfs(i - 2) + counter[i])
            return dp[i]

        return dfs(max_num)
