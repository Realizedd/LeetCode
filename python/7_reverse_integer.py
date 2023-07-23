import math


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MIN, MAX = -2 ** 31, 2 ** 31 - 1

        while x:
            last_digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and last_digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and last_digit < MIN % 10):
                return 0

            res = (res * 10) + last_digit

        return res


sol = Solution()
print(sol.reverse(123))