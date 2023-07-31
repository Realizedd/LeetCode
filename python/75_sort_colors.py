from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        ones = 0

        while left < right and right - left + 1 > ones:
            if nums[right] == 2:
                right -= 1
                continue

            if nums[left] == 0:
                left += 1
                continue

            if nums[left] == 1:
                nums[left] = 0
                ones += 1
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        last_zero = left - 1

        while left <= right:
            if nums[left] == 0:
                nums[left] = 1
                left += 1
                ones -= 1
                continue

            if nums[left] == 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

            nums[last_zero] = 1
            last_zero -= 1
            ones -= 1

        while ones:
            nums[last_zero] = 1
            last_zero -= 1
            ones -= 1


sol = Solution()
sol.sortColors([1,1,0])


