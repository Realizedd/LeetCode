from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_max = 0

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            freq_max = max(freq_max, freq[n])

        rev = {}

        for key in freq:
            ls = rev.get(freq[key], [])
            ls.append(key)
            rev[freq[key]] = ls

        res = []
        ls = rev[freq_max]

        while k > 0:
            if not ls:
                freq_max -= 1

                if freq_max not in rev:
                    continue

                ls = rev[freq_max]

            res.append(ls.pop())
            k -= 1

        return res


sol = Solution()
print(sol.topKFrequent([5,3,1,1,1,3,73,1], 2))
