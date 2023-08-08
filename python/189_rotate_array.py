from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr: list, start: int, end: int) -> None:
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1

        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        pivot = n - k
        rotated = nums[pivot:] + nums[:pivot]

        for i in range(len(nums)):
            nums[i] = rotated[i]

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        for _ in range(k):
            prev = nums[0]

            for i in range(1, n):
                temp = nums[i]
                nums[i] = prev
                prev = temp

            nums[0] = prev
