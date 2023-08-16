from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sum_arr = [0] * n
        sum_arr[0] = nums[0]

        for i in range(1, n):
            sum_arr[i] = nums[i] + sum_arr[i - 1]

        if sum_arr[n - 1] - sum_arr[0] == 0:
            return 0

        for i in range(1, n):
            if sum_arr[i - 1] == sum_arr[n - 1] - sum_arr[i]:
                return i

        return -1