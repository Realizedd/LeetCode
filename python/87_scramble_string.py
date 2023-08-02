class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}

        def dfs(length, i, j):
            if (length, i, j) in dp:
                return dp[(length, i, j)]
            if length == 1:
                dp[(length, i, j)] = s1[i] == s2[j]
                return dp[(length, i, j)]

            res = False

            for k in range(1, length):
                res |= dfs(k, i, j) and dfs(length - k, i + k, j + k)
                res |= dfs(k, i, j + length - k) and dfs(length - k, i + k, j)

            dp[(length, i, j)] = res
            return res

        return dfs(len(s1), 0, 0)


sol = Solution()
print(sol.isScramble('athatscoolandawesome', 'andawesomeathatscool'))
