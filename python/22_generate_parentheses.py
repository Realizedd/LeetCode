from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generateRecParen(cur, open, close):
            if len(cur) == n + n:
                res.append(cur)
                return

            if open > 0:
                generateRecParen(cur + '(', open - 1, close)

            if close > open:
                generateRecParen(cur + ')', open, close - 1)

        generateRecParen('', n, n)
        return res


sol = Solution()
print(sol.generateParenthesis(3))