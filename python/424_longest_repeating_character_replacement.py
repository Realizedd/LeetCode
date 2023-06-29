class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rep_max = 0
        hmap = {}
        most_freq = s[0]
        start = 0

        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1

            if hmap[s[i]] > hmap[most_freq]:
                most_freq = s[i]

            if (i - start + 1) - hmap[most_freq] > k:
                hmap[s[start]] -= 1
                start += 1

            rep_max = max(rep_max, i - start + 1)

        return rep_max


sol = Solution()
print(sol.characterReplacement('AABA', 0))
