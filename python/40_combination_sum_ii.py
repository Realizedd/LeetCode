from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(cur_sum, cur, idx):
            if cur_sum == target:
                res.append(cur.copy())
                return
            elif cur_sum > target or idx == len(candidates):
                return

            # Choose candidates[idx]
            cur.append(candidates[idx])
            dfs(cur_sum + candidates[idx], cur, idx + 1)
            cur.pop()

            # Skip duplicates
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1

            # Don't choose candidates[idx]
            dfs(cur_sum, cur, idx + 1)

        dfs(0, [], 0)
        return res