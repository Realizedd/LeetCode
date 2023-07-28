from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(arr, cur):
            if not arr:
                res.append(cur.copy())
                return

            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue

                cur.append(nums[i])
                dfs(arr[:i] + arr[i + 1:], cur)
                cur.pop()

        dfs(nums, [])
        return res
