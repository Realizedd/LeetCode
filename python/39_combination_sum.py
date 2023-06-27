from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur, total, index):
            if total == target:
                res.append(cur.copy())
                return
            elif total > target or index >= len(candidates):
                return

            for j in range(0, ((target - total) // candidates[index]) + 1):
                for k in range(1, j + 1):
                    cur.append(candidates[index])

                backtrack(cur, total + candidates[index] * j, index + 1)

                for k in range(1, j + 1):
                    cur.pop()

        backtrack([], 0, 0)
        return res


sol = Solution()
print(sol.combinationSum([8,7,4,3], 11))
