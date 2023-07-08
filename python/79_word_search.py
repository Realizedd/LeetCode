from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(path, r, c, idx):
            if len(path) == len(word):
                return True
            if m <= r or r < 0 or n <= c or c < 0 or board[r][c] != word[idx] or (r,c) in path:
                return False

            path.add((r, c))

            res = False
            res |= dfs(path, r + 1, c, idx + 1)
            res |= dfs(path, r, c + 1, idx + 1)
            res |= dfs(path, r - 1, c, idx + 1)
            res |= dfs(path, r, c - 1, idx + 1)

            path.remove((r, c))
            return res

        for row in range(m):
            for col in range(n):
                if dfs(set(), row, col, 0):
                    return True

        return False
