from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        normal, rotten = 0, deque()
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    normal += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        mins = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while rotten and normal > 0:
            cur_rotten = len(rotten)

            for i in range(cur_rotten):
                r, c = rotten.popleft()

                for direction in dirs:
                    cur_r, cur_c = r + direction[0], c + direction[1]

                    if cur_r in range(m) and cur_c in range(n) and grid[cur_r][cur_c] == 1:
                        grid[cur_r][cur_c] = 2
                        rotten.append((cur_r, cur_c))
                        normal -= 1

            mins += 1

        return mins if normal == 0 else -1