"""
# Prepare adjacency matrix (include itself as well)
# Maintain result array
# Traverse queries
    - if query's first element is 1 -> maintenance
        - check for the neighbors of 1
        - find the minimum 
        - append the minimum in result array
        - if no value present for it return -1

    - if query's first element is 2 -> make it offline
        - need to delete that element from adjacency matrix
        - but before removing key
            - access its value, for each node in its value list, access and delete it from their value list
# return result array

"""
from collections import defaultdict
import heapq
from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)
        
        # Step 1: Build connected components using DSU
        for u, v in connections:
            dsu.union(u, v)
        
        # Step 2: Initialize a min-heap for each component
        comp_heap = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            heapq.heappush(comp_heap[root], i)
        
        # Step 3: Track online/offline status
        online = [True] * (c + 1)
        res = []
        
        # Step 4: Process each query
        for q, x in queries:
            root = dsu.find(x)

            # Query type 1: Maintenance check
            if q == 1:
                if online[x]:
                    res.append(x)
                else:
                    # Remove offline stations from the top of the heap
                    while comp_heap[root] and not online[comp_heap[root][0]]:
                        heapq.heappop(comp_heap[root])
                    
                    # If any station is still online, return the smallest
                    if comp_heap[root]:
                        res.append(comp_heap[root][0])
                    else:
                        res.append(-1)

            # Query type 2: Mark a station offline
            elif q == 2:
                online[x] = False

        return res
