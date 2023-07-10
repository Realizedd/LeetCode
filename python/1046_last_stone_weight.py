import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            larger, smaller = -heapq.heappop(stones), -heapq.heappop(stones)

            if larger > smaller:
                heapq.heappush(stones, -(larger - smaller))

        return -stones[0] if stones else 0
