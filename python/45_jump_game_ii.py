from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = n - 1
        j = 0

        while end > 0:
            farthest = n

            for i in range(end - 1, -1, -1):
                if i + nums[i] >= end:
                    farthest = min(farthest, i)

            end = farthest
            j += 1

        return j

    # Optimized BFS-like solution
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curFarthest = 0, 0, 0

        for i in range(len(nums)):
            curFarthest = max(curFarthest, i + nums[i])

            if i == curEnd:
                jumps += 1
                curEnd = curFarthest

        return jumps
