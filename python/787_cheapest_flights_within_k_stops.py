from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1  # Include start

        graph = defaultdict(dict)

        for source, destination, price in flights:
            graph[source][destination] = price

        min_costs = [float('inf')] * n
        min_costs[src] = 0

        queue = deque()
        queue.append((src, 0))

        while queue and k:
            sz = len(queue)
            k -= 1

            for _ in range(sz):
                dest, cost = queue.popleft()

                for ndest in graph[dest]:
                    total_cost = cost + graph[dest][ndest]

                    if total_cost < min_costs[ndest]:
                        min_costs[ndest] = total_cost
                        queue.append((ndest, total_cost))

        return min_costs[dst] if min_costs[dst] != float('inf') else -1
