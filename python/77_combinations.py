from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(start, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return

            need = k - len(cur)
            remain = n - start + 1
            available = remain - need

            for i in range(start, start + available + 1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()

        dfs(1, [])
        return res
