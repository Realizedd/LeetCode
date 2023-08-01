class Solution:
    def totalNQueens(self, n: int) -> int:
        col_queens, pos_queens, neg_queens = set(), set(), set()

        def nQueens(r):
            if r == n:
                return 1

            total = 0

            for c in range(n):
                if c in col_queens or (r + c) in pos_queens or (r - c) in neg_queens:
                    continue

                col_queens.add(c)
                pos_queens.add(r + c)
                neg_queens.add(r - c)
                total += nQueens(r + 1)
                col_queens.remove(c)
                pos_queens.remove(r + c)
                neg_queens.remove(r - c)

            return total

        return nQueens(0)
