from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start, end = 0, n - 1
        maxwater = 0

        while start < end:
            maxwater = max(maxwater, (end - start) * min(height[start], height[end]))

            if height[start] < height[start + 1]:
                start += 1
            elif height[end] < height[end - 1]:
                end -= 1
            else:
                end -= 1
                start += 1

        return maxwater

    def maxAreaBF(self, height: List[int]) -> int:
        n = len(height)
        maxwater = 0

        for i in range(0, n):
            for j in range(i + 1, n):
                maxwater = max(maxwater, abs(i - j) * min(height[i], height[j]))

        return maxwater


sol = Solution()
print(sol.maxAreaDP([1,8,6,2,5,4,8,3,7]))