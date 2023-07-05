from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        # b must be longer
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        start, end = 0, m

        while start <= end:
            midA = (start + end) // 2
            midB = (m + n + 1) // 2 - midA
            maxLeftA = float('-inf') if midA == 0 else a[midA - 1]
            minRightA = float('inf') if midA == m else a[midA]
            maxLeftB = float('-inf') if midB == 0 else b[midB - 1]
            minRightB = float('inf') if midB == n else b[midB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 != 0:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            elif maxLeftA > minRightB:
                end = midA - 1
            else:
                start = midA + 1