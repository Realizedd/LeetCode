from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False

        # Idea: Use 1st row & 1st col to mark zero rows and cols
        for r in range(m):
            for c in range(n):
                if not matrix[r][c]:
                    if not r: first_row_zero = True
                    if not c: first_col_zero = True
                    matrix[0][c] = matrix[r][0] = 0

        for r in range(1, m):
            for c in range(1, n):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0