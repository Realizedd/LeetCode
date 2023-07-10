import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(p[0] ** 2 + p[1] ** 2, [p[0], p[1]]) for p in points]
        print(points)
        heapq.heapify(points)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(points)[1])

        return res
