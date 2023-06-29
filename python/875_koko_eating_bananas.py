import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pmax = max(piles)
        left, right = 1, pmax - 1
        min_k = pmax

        while left <= right:
            k = (right + left) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile / k)

            if total <= h:
                min_k = min(min_k, k)
                right = k - 1
            else:
                left = k + 1

        return min_k


sol = Solution()
print(sol.minEatingSpeed([2,2], 2))