from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_total = (n * (n + 1)) // 2
        total = sum(nums)
        return expected_total - total

    def missingNumberBits(self, nums: List[int]) -> int:
        a = 0

        for n in nums:
            a ^= n

        for n in range(1, len(nums) + 1):
            a ^= n

        return a