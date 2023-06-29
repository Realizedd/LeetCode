from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec_permute(cur, rem):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(0, len(rem)):
                cur.append(rem[i])
                rec_permute(cur, rem[:i] + rem[(i + 1):len(rem)])
                cur.pop()

        rec_permute([], nums)
        return res


sol = Solution()
print(sol.permute([1,2,3]))
