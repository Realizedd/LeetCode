from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            res[i] = res[n + i] = nums[i]

        return res
