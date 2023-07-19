import heapq
from collections import defaultdict
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        counter = defaultdict(int)

        for h in hand:
            counter[h] += 1

        heapq.heapify(hand)

        for j in range(len(hand) // groupSize):
            start = heapq.heappop(hand)

            while not counter[start]:
                start = heapq.heappop(hand)

            for i in range(groupSize):
                if not counter[start]:
                    return False

                counter[start] -= 1
                start += 1

        return True