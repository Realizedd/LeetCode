from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1

        for i in range(n - 1, 0, -1):
            if digits[i] > 9:
                digits[i] %= 10
                digits[i - 1] += 1
            else:
                break

        if digits[0] > 9:
            digits[0] %= 10
            return [1] + digits

        return digits
