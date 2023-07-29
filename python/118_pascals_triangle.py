from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            newRow = [1]

            for j in range(1, len(res[-1])):
                newRow.append(res[-1][j - 1] + res[-1][j])

            newRow.append(1)
            res.append(newRow)

        return res