from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        mapping = {}

        for i in range(len(s)):
            mapping[s[i]] = i

        start, end = 0, -1

        for i in range(len(s)):
            end = max(end, mapping[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
