from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]

        for n in nums:
            copy = [i.copy() for i in powerset]

            for ls in copy:
                ls.append(n)

            powerset += copy
            print(powerset)

        return powerset

    def subsetsBacktracking(self, nums: List[int]) -> List[List[int]]:
        powerset = []

        def backtrack(powerset, nums, cur, index):
            powerset.append(cur.copy())

            for i in range(index, len(nums)):
                cur.append(nums[i])
                backtrack(powerset, nums, cur, i + 1)
                cur.pop()

        backtrack(powerset, nums, [], 0)
        return powerset


sol = Solution()
print(sol.subsetsBacktracking([1,2]))