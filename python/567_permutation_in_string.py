class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        n = len(s1)

        for c in s1:
            target[ord(c) - ord('a')] += 1

        chars = [0] * 26

        for i in range(len(s2)):
            if i >= n:
                chars[ord(s2[i - n]) - ord('a')] -= 1

            chars[ord(s2[i]) - ord('a')] += 1
            print(chars)

            if target == chars:
                return True

        return False


sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))