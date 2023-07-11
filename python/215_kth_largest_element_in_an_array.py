import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, ptr = nums[r], l

            for idx in range(l, r):
                if nums[idx] <= pivot:
                    nums[ptr], nums[idx] = nums[idx], nums[ptr]
                    ptr += 1

            nums[r], nums[ptr] = nums[ptr], nums[r]

            if ptr == k:
                return nums[ptr]
            elif ptr > k:
                return quickSelect(l, ptr - 1)
            else:
                return quickSelect(ptr + 1, r)

        return quickSelect(0, len(nums) - 1)
