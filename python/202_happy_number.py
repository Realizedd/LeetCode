class Solution:

    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            next = 0

            while n:
                next += (n % 10) ** 2
                n //= 10

            if next in seen:
                return False

            if next == 1:
                return True

            seen.add(next)
            n = next


sol = Solution()
print(sol.isHappy(2))