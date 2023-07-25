from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        visited = set()
        dist = 0

        while queue:
            sz = len(queue)

            for _ in range(sz):
                curRow, curCol = queue.popleft()
                rooms[curRow][curCol] = min(dist, rooms[curRow][curCol])

                for addRow, addCol in DIRECTIONS:
                    nRow, nCol = curRow + addRow, curCol + addCol

                    if nRow in range(m) and nCol in range(n) and (nRow, nCol) not in visited and rooms[nRow][nCol] >= 0:
                        visited.add((nRow, nCol))
                        queue.append((nRow, nCol))

            dist += 1


sol = Solution()
print(sol.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))