class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def seq(idx, j):
            if j == len(t):
                return 1
            if idx == len(s):
                return 0
            if (idx, j) in dp:
                return dp[(idx, j)]

            res = seq(idx + 1, j)

            if s[idx] == t[j]:
                res += seq(idx + 1, j + 1)

            dp[(idx, j)] = res
            return res

        return seq(0, 0)

