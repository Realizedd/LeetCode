from typing import List


class Solution:
    def getRow(self, n: int) -> List[int]:
        res = [1]

        for r in range(1, n + 1):
            prev = res[r - 1]
            res.append(((n - r + 1) * prev) // r)

        return res
