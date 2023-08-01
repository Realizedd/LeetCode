from collections import deque
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = n - 1
        j = m - 1

        for idx in range(m + n - 1, -1, -1):
            if i < 0:
                break

            if j >= 0 and nums1[j] > nums2[i]:
                nums1[idx] = nums1[j]
                j -= 1
            elif i >= 0:
                nums1[idx] = nums2[i]
                i -= 1


sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))