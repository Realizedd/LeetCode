import heapq
from collections import defaultdict


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1

        heap = [(-counter[c], c) for c in counter]
        heapq.heapify(heap)

        res = ''

        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            res += ch1
            cnt1 += 1

            if cnt1 < 0:
                if not heap:
                    return ''

                cnt2, ch2 = heapq.heappop(heap)
                res += ch2
                cnt2 += 1
                heapq.heappush(heap, (cnt1, ch1))

                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))

        return res
