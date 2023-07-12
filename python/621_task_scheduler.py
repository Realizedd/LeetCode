import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total = len(tasks)
        counter = [0] * 26

        for task in tasks:
            counter[ord(task) - ord('A')] += 1

        counter = [[-v, chr(i + ord('A'))] for i, v in enumerate(counter) if v > 0]
        heapq.heapify(counter)

        mins = 0
        queue = deque()

        while (counter or queue) and total > 0:
            mins += 1

            if counter:
                cur = heapq.heappop(counter)
                print(cur[1])
                cur[0] += 1
                queue.append(cur)
                total -= 1
            else:
                queue.append([0, 0])
                print('idle')

            if len(queue) > n:
                elem = queue.popleft()

                if elem[0] < 0:
                    heapq.heappush(counter, elem)

        return mins


sol = Solution()
print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))