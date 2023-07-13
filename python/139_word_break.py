from typing import List


class Solution:
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


sol = Solution()
print(sol.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"]))