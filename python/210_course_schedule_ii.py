from typing import List


class Solution:
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {idx: [] for idx in range(numCourses)}

        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        path = []
        visiting, visited = set(), set()

        def dfs(idx):
            if idx in visited:
                return True
            if idx in visiting:
                return False

            visiting.add(idx)

            for pre in adj[idx]:
                if not dfs(pre):
                    return False

            visiting.remove(idx)
            visited.add(idx)
            path.append(idx)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return path

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class Node:
            def __init__(self, idx: int):
                self.idx = idx
                self.children = set()

        graph = [Node(i) for i in range(numCourses)]

        for p in prerequisites:
            graph[p[1]].children.add(graph[p[0]])

        path = []

        while graph:
            incoming = {}

            for node in graph:
                if node not in incoming:
                    incoming[node] = 0

                for child in node.children:
                    if child not in incoming:
                        incoming[child] = 0

                    incoming[child] += 1

            found_start = False

            for node in incoming:
                if incoming[node] == 0:
                    path.append(node.idx)
                    found_start = True
                    graph.remove(node)

            if not found_start and graph:
                return []

        return path
