from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first, last = i + 1, n - 1

            while first < last:
                if nums[first] + nums[last] == -nums[i]:
                    res.append([nums[first], nums[last], nums[i]])

                    while first < n - 1 and nums[first] == nums[first + 1]:
                        first += 1

                    while last > 1 and nums[last] == nums[last - 1]:
                        last -= 1

                    first += 1
                    last -= 1
                elif nums[first] + nums[last] < -nums[i]:
                    first += 1
                else:
                    last -= 1

        return res


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
