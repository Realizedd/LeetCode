from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid // m][mid % m] == target:
                return True
            elif matrix[mid // m][mid % m] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
