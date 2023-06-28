from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        maxsum = nums[0]

        for i in range(1, len(nums)):
            cur = cur + nums[i] if cur + nums[i] > nums[i] else nums[i]

            if cur > maxsum:
                maxsum = cur

        return maxsum
