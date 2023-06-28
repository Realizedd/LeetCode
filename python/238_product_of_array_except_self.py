from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1:
            return nums

        res = [0] * n
        res[0] = 1
        left_prod = nums[0]

        for i in range(1, n):
            res[i] = left_prod
            left_prod *= nums[i]

        print(res)

        right_prod = nums[n - 1]

        for j in range(n - 2, -1, -1):
            res[j] *= right_prod
            right_prod *= nums[j]

        print(res)
        return res


sol = Solution()
sol.productExceptSelf([4,3,2,1,2])