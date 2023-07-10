from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = [['.'] * n for _ in range(n)]
        col, pos_diag, neg_diag = set(), set(), set()

        def dfs(r):
            if r == n:
                res.append([''.join(x) for x in cur])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                cur[r][c] = 'Q'
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                dfs(r + 1)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                col.remove(c)
                cur[r][c] = '.'

        dfs(0)
        return res


sol = Solution()
print(sol.solveNQueens(8))
