from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        invalid_os = set()

        def dfs(r, c):
            if r not in range(m) or c not in range(n) or board[r][c] == 'X' or (r, c) in invalid_os:
                return

            invalid_os.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row, col) not in invalid_os:
                    board[row][col] = 'X'
