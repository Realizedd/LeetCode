from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        res[0][0] = 1

        if n < 2:
            return res

        start, end = 0, n - 1

        while start < end:
            for c in range(start + 1, end + 1):
                res[start][c] = res[start][c - 1] + 1

            for r in range(start + 1, end + 1):
                res[r][end] = res[r - 1][end] + 1

            for c in range(end - 1, start - 1, -1):
                res[end][c] = res[end][c + 1] + 1

            for r in range(end - 1, start, -1):
                res[r][start] = res[r + 1][start] + 1

            last = res[start + 1][start]
            start += 1
            end -= 1

            if start <= end:
                res[start][start] = last + 1

        return res


sol = Solution()
for i in range(2, 10):
    for r in sol.generateMatrix(i): print(r)

