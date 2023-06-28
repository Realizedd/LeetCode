class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_sub = 0
        dic = {}
        start = 0

        for i in range(n):
            if s[i] in dic:
                start = max(start, dic[s[i]] + 1)

            dic[s[i]] = i
            max_sub = max(max_sub, i - start + 1)

        return max_sub


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
