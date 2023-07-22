import math
from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0

        for pt in self.pts:
            if (abs(pt[1] - point[1]) != abs(pt[0] - point[0])) or point[0] == pt[0] and point[1] == pt[1]:
                continue

            if (pt[0], point[1]) in self.pts and (point[0], pt[1]) in self.pts:
                res += self.pts[pt] * self.pts[(pt[0], point[1])] * self.pts[(point[0], pt[1])]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
sol = DetectSquares()
sol.add([-10, 0])
sol.add([0, 0])
sol.add([-10, 10])
print(sol.count([0, 10]))