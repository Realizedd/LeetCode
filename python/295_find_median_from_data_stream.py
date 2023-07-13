import heapq


class MedianFinder:

    def __init__(self):
        self.smallerHeap = []
        self.largerHeap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if num < (self.largerHeap[0] if self.largerHeap else float('inf')):
            heapq.heappush(self.smallerHeap, -num)
        else: # num >= minLarger
            heapq.heappush(self.largerHeap, num)

        if len(self.smallerHeap) > len(self.largerHeap):
            heapq.heappush(self.largerHeap, -heapq.heappop(self.smallerHeap))
        elif len(self.smallerHeap) < len(self.largerHeap):
            heapq.heappush(self.smallerHeap, -heapq.heappop(self.largerHeap))

        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.smallerHeap[0] + self.largerHeap[0]) / 2
        return -self.smallerHeap[0] if len(self.smallerHeap) > len(self.largerHeap) else self.largerHeap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(1)
obj.addNum(3)
obj.addNum(4)

for i in range(10):
    obj.addNum(i)

print(obj.findMedian())