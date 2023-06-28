from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[j][n - i - 1], matrix[i][j] = matrix[i][j], matrix[j][n - i - 1]
                matrix[n - i - 1][n - j - 1], matrix[i][j] = matrix[i][j], matrix[n - i - 1][n - j - 1]
                matrix[n - j - 1][i], matrix[i][j] = matrix[i][j], matrix[n - j - 1][i]


sol = Solution()
sol.rotate([[1,2,3,4],[4,5,6,8],[7,8,9,10],[7,8,9,10]])
