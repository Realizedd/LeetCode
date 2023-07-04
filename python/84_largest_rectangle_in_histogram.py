from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rec = 0

        for i, h in enumerate(heights):
            st = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_rec = max(max_rec, (i - idx) * height)
                st = idx

            stack.append((st, h))

        while stack:
            idx, height = stack.pop()
            max_rec = max(max_rec, (len(heights) - idx) * height)

        return max_rec

    def largestRectangleAreaDP(self, heights: List[int]) -> int:
        n = len(heights)
        dp = [[0] * n for _ in range(n)]
        largest = 0

        for i in range(n):
            dp[i][i] = heights[i]
            largest = max(largest, dp[i][i])

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = min(heights[i], heights[j])

                if j - i > 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])

                largest = max(largest, (j - i + 1) * dp[i][j])

        return largest


sol = Solution()
print(sol.largestRectangleArea([3,6,5,7,4,8,1,0]))