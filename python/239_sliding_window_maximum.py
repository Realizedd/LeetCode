from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        queue = deque()

        for i in range(0, n):
            while queue and queue[-1] < nums[i]:
                queue.pop()

            queue.append(nums[i])

            if i >= k - 1:
                if i - k >= 0 and nums[i - k] == queue[0]:
                    queue.popleft()

                ans.append(queue[0])

        return ans


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

