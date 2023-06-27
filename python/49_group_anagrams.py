from typing import List


class Solution:
    def makeTuple(self, s):
        ls = [0] * 26

        for c in s:
            ls[ord(c) - ord('a')] += 1

        return tuple(ls)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap: (str, List[str]) = {}

        for s in strs:
            k = self.makeTuple(s)
            ls = hmap.get(k, [])
            ls.append(s)
            hmap[k] = ls

        return list(hmap.values())

    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
        hmap: (str, List[str]) = {}

        for s in strs:
            v = ''.join(sorted(s))
            ls = hmap.get(v, [])
            ls.append(s)
            hmap[v] = ls

        return list(hmap.values())
