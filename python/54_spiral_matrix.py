from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = set()
        path = []
        directions = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }

        def dfs(r, c, direction):
            if len(path) >= m * n:
                return

            visited.add((r, c))
            path.append(matrix[r][c])
            print(r, c, matrix[r][c])

            if r + direction[0] not in range(m) or c + direction[1] not in range(n) or (r + direction[0], c + direction[1]) in visited:
                direction = directions[direction]

            dfs(r + direction[0], c + direction[1], direction)

        dfs(0, 0, (0, 1))
        return path


sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))