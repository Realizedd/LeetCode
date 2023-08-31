from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reachable = [0] * (n + 1)

        for i, r in enumerate(ranges):
            start, end = max(0, i - r), min(n, i + r)
            reachable[start] = max(reachable[start], end)

        cur_end, next_end, cnt = 0, 0, 0

        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > cur_end:
                cnt += 1
                cur_end = next_end

            next_end = max(next_end, reachable[i])

        return cnt