from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Parent Array
        par = [i for i in range(n)]
        # Rank Array
        rank = [1] * n

        # Function to find parent element
        def find(n1):
            res = n1
            # Loop will stop only if the element is parent of itself
            while res != par[res]:
                # Path Compression 
                par[res] = par[par[res]]
                res = par[res]
            return res

        # Function to find union of two elements
        def union(n1, n2):
            # Getting roots of both nodes
            p1, p2 = find(n1), find(n2) 
            # If both roots are same, it means they are already connected
            if p1 == p2:
                return 0

            # Checking which node's rank is bigger, attach smaller tree under larger
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

