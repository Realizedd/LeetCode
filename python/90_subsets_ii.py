from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        powerset = []

        def backtrack(powerset, nums, cur, index):
            print(cur)
            powerset.append(cur.copy())

            i = index

            while i < len(nums):
                cur.append(nums[i])
                backtrack(powerset, nums, cur, i + 1)
                cur.pop()
                i += 1

                while 0 < i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1

        backtrack(powerset, nums, [], 0)
        return powerset


sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
