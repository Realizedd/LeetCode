from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[end] > nums[mid]:
                end = mid
            else:
                start = mid + 1

        return nums[start]


sol = Solution()
print(sol.findMin([4,5,6,7,0,1,2]))
