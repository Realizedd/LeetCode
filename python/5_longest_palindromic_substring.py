class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = (0, 0)

        for i in range(n):
            res = self.longestPalindromeRec(s, i, i)

            if res[1] - res[0] > longest[1] - longest[0]:
                longest = res

            if i < n - 1 and s[i] == s[i + 1]:
                res = self.longestPalindromeRec(s, i, i + 1)

                if res[1] - res[0] > longest[1] - longest[0]:
                    longest = res

        return s[longest[0]:(longest[1] + 1)]

    def longestPalindromeRec(self, s, begin, end):
        if begin == 0 or end == len(s) - 1 or s[begin - 1].lower() != s[end + 1].lower():
            return begin, end
        return self.longestPalindromeRec(s, begin - 1, end + 1)

    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest = (0, 0)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if j - i > longest[1] - longest[0]:
                        longest = (i, j)

        return s[longest[0]:(longest[1]+1)]


sol = Solution()
print(sol.longestPalindromeDP('babdadaddda'))
