import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        minHeap = []
        res = 0

        for start, end in intervals:
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, end)

            res = max(res, len(minHeap))

        return res