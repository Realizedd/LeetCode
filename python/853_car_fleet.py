from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position) # Consider all cars as fleets initially
        position = sorted(enumerate(position), key=lambda p: p[1])
        prev = len(position) - 1

        for i in range(len(position) - 2, -1, -1):
            p = position[i]
            f = position[prev]

            if (target - p[1]) / speed[p[0]] <= (target - f[1]) / speed[f[0]]:
                fleets -= 1
            else:
                prev = i

        return fleets


sol = Solution()
print(sol.carFleet(target = 10, position = [0,4,2], speed = [2,1,3]))