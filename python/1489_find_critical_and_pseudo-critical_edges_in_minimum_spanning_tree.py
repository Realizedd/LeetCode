from typing import List


# Union Find implementation with path compression and union-by-rank
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]

        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(n)
        mst_weight = 0

        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo = [], []

        for n1, n2, e_weight, idx in edges:
            # Try building mst without cur edge for critical edge check
            uf = UnionFind(n)
            weight = 0

            for v1, v2, w, i in edges:
                if idx != i and uf.union(v1, v2):
                    weight += w

            if max(uf.rank) != n or weight > mst_weight:
                critical.append(idx)
                continue

            # Try building mst with cur edge for pseudo-critical edge check
            uf = UnionFind(n)
            weight = e_weight
            uf.union(n1, n2)

            for v1, v2, w, i in edges:
                if uf.union(v1, v2):
                    weight += w

            if weight == mst_weight:
                pseudo.append(idx)

        return [critical, pseudo]
