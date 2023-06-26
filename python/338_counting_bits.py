import math
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # LSB Approach.
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = 1 + dp[i - 2 ** math.floor(math.log2(i))]

        return dp

    def countBitsRSB(self, n: int) -> List[int]:
        # RSB Approach.
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = (i & 1) + dp[i >> 1]

        return dp


sol = Solution()
print(sol.countBits(16))
