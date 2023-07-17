from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                res.append(newInterval)
                return res + intervals[i:]

        res.append(newInterval)
        return res


sol = Solution()
print(sol.insert([[1,3],[6,9]], [7,8]))



