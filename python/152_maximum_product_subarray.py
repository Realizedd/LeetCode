from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        r = nums[0]

        for i in range(len(nums)):
            n = nums[i]
            prod *= n
            r = max(r, prod)

            if n == 0:
                prod = 1

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            prod *= n
            r = max(r, prod)

            if n == 0:
                prod = 1
        return r


sol = Solution()
print(sol.maxProduct([2,-5,-2,-4,3]))