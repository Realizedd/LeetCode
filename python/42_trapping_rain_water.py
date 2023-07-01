from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_max, right_max = 0, len(height) - 1
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                if height[left] <= height[left_max]:
                    water += height[left_max] - height[left]
                else:
                    left_max = left

                left += 1
            else:
                if height[right] <= height[right_max]:
                    water += height[right_max] - height[right]
                else:
                    right_max = right

                right -= 1

        return water

    def trapIterative(self, height: List[int]) -> int:
        water = 0
        cur_max = 0
        cur_water = 0

        for i in range(1, len(height)):
            if height[i] <= height[cur_max]:
                cur_water += height[cur_max] - height[i]
            else:
                water += cur_water
                cur_max = i
                cur_water = 0

        cur_water = 0
        last_max = cur_max
        cur_max = len(height) - 1

        for i in range(len(height) - 1, last_max - 1, -1):
            if height[i] <= height[cur_max]:
                cur_water += height[cur_max] - height[i]
            else:
                water += cur_water
                cur_max = i
                cur_water = 0

        return water


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
