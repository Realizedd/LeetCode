from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def generate(cur, idx):
            if idx == len(digits):
                res.append(cur)
                return

            for c in mapping[digits[idx]]:
                generate(cur + c, idx + 1)

        if digits:
            generate('', 0)
        return res
