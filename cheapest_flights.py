from typing import List
from collections import defaultdict
from queue import PriorityQueue


class Solution:


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = defaultdict(dict) # create graph

        for s, d, p in flights:
            graph[s][d] = p

        if K == 0: # When there are no stops allower (k = 0), try to find direct path
            if dst in graph[src]:
                return graph[src][dst]
            else:
                return -1

        pq = PriorityQueue()
        pq.put((0, src, 0))

        while not pq.empty():
            price, city, stops_count = pq.get()

            if ((stops_count >= K+1) and (city != dst)):
                continue

            if city == dst:
                return price


            for stop in graph[city]:
                pq.put((price + graph[city][stop], stop, stops_count+1))

        return -1


n = 6
edges = [[2,3,87],[4,3,55],[2,5,27],[0,2,28],[0,3,55],[5,0,48],[1,3,37],[2,1,13],[5,3,8],[5,4,82]]
src = 0
dst = 3
k = 0

sol = Solution()
print(sol.findCheapestPrice(n, edges, src, dst, k))
