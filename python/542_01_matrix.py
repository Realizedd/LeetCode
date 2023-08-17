from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        queue, visited = deque(), set()

        for cur_row in range(m):
            for cur_col in range(n):
                if mat[cur_row][cur_col] == 0:
                    queue.append((cur_row, cur_col))
                    visited.add((cur_row, cur_col))

        dist = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row, col))

                if mat[row][col] == 1:
                    res[row][col] = dist

                for direction in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                    n_row, n_col = row + direction[0], col + direction[1]

                    if n_row in range(m) and n_col in range(n) and (n_row, n_col) not in visited:
                        queue.append((n_row, n_col))
                        visited.add((n_row, n_col))

            dist += 1

        return res
