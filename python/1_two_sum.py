from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}

        for i in range(len(nums)):
            v = target - nums[i]

            if v in hset:
                return [i, hset[v]]

            hset[nums[i]] = i

        return [-1, -1]


sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 5], 7))
