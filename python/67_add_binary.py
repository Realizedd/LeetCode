from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = deque()
        i, j = len(a) - 1, len(b) - 1
        carry = False

        while i >= 0 or j >= 0:
            total = 1 if carry else 0

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            carry = total > 1
            res.appendleft(total % 2)

        if carry:
            res.appendleft(1)

        return ''.join(res)
