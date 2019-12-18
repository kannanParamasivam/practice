from typing import List
from collections import deque

class TopologicalSorter:


    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.vertices = [v for v in range(len(graph))]
        self.visited = [False for v in range(len(graph))]
        self.TS_result = deque()


    def topological_sort(self):
        ts_result = deque()

        for vertex in self.vertices:

            if not self.visited[vertex]:
                self.dfs(vertex, ts_result)

        return ts_result


    def dfs(self, vertex:int, ts_result:deque):

        if self.visited[vertex]:
            return

        self.visited[vertex] = True

        for adj_vertex in self.graph[vertex]:
            self.dfs(adj_vertex, ts_result)

        ts_result.appendleft(vertex)


graph = [[],
         [],
         [3],
         [1],
         [0, 1],
         [0, 2]]

topological_sorter = TopologicalSorter(graph)
print(topological_sorter.topological_sort())