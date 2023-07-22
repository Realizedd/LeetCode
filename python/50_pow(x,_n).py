class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x is guaranteed to not be a 0 when n = 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        ans = 1

        while n > 0:
            if n & 1:
                ans *= x

            n //= 2
            x *= x

        return ans
