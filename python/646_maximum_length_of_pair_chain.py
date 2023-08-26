from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        ans = 1
        prev = pairs[0]

        for i in range(1, len(pairs)):
            if prev[1] >= pairs[i][0]:
                continue

            ans += 1
            prev = pairs[i]

        return ans