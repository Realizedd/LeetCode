from typing import List


class Node:
    def __init__(self, idx: int):
        self.idx = idx
        self.children = set()


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [Node(i) for i in range(numCourses)]

        for p in prerequisites:
            graph[p[1]].children.add(graph[p[0]])

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
                    found_start = True
                    graph.remove(node)

            if not found_start and graph:
                return False

        return True
