class Solution:
    def isPalindrome(self, s: str) -> bool:
        res, count = "", 0

        for c in s:
            if c.isalnum():
                res += c.lower()
                count += 1

        for i in range(count // 2):
            if res[i] != res[count - i - 1]:
                return False

        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
