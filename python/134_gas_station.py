from typing import List


class Solution:
    def canCompleteCircuitBruteForce(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            tank = gas[i]

            if cost[i] > tank:
                continue

            reachable = True
            prev = i

            for j in range(1, n + 1):
                next = (i + j) % n
                tank -= cost[prev]

                if tank < 0:
                    reachable = False
                    break

                tank += gas[next]

            if reachable:
                return i

        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        total, cur_total = 0, 0
        lastPos = -1

        for i in range(n):
            total += gas[i] - cost[i]
            cur_total += gas[i] - cost[i]

            if cur_total < 0:
                cur_total = 0
                lastPos = i

        return lastPos + 1 if total >= 0 else -1
