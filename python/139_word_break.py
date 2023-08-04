from typing import List


class Solution:
    # Top-Down Memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [-1] * len(s)

        def match(idx):
            if idx == len(s):
                return True
            if dp[idx] != -1:
                return dp[idx]

            for i in range(idx, len(s)):
                if s[idx:(i + 1)] in wordDict and match(i + 1):
                    dp[i] = 1
                    return True

            dp[idx] = 0
            return False

        return match(0)

    # Bottom-Up Tabulation
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [0] * len(s)

        for j in range(len(s) - 1, -1, -1):
            if s[j:] in wordDict:
                dp[j] = 1

        for i in range(len(s) - 2, -1, -1):
            for j in range(i, -1, -1):
                if s[j:i + 1] in wordDict and dp[i + 1]:
                    dp[j] = 1

        return dp[0] == 1




sol = Solution()
print(sol.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))