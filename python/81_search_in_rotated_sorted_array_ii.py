from typing import List


class Solution:
    def findMin(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            while left < right and arr[right] == arr[right - 1]:
                right -= 1

            mid = (left + right) // 2

            if arr[mid] < arr[right]:
                right = mid
            else:
                left = mid + 1

        while left > 0 and arr[left] == arr[left - 1]:
            left -= 1

        return left

    def search(self, nums: List[int], target: int) -> bool:
        pivot, n = self.findMin(nums), len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[(mid + pivot) % n] == target:
                return True
            elif nums[(mid + pivot) % n] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


sol = Solution()
print(sol.findMin([1,1,1,1,3]))