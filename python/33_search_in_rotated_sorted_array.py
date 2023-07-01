from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            start, end = 0, len(nums) - 1

            while start < end:
                mid = (start + end) // 2

                if nums[end] > nums[mid]:
                    end = mid
                else:
                    start = mid + 1

            return start

        r = findMin(nums) # Rotation factor
        l = len(nums)
        left, right = 0, l - 1

        while left <= right:
            mid = (left + right) // 2
            conv = (mid + r) % l
            print("mid=", mid, "conv=", conv)

            if nums[conv] == target:
                return conv
            elif nums[conv] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


sol = Solution()
for i in range(0, 8):
    print(i, "is at", sol.search([4,5,6,7,0,1,2], i))