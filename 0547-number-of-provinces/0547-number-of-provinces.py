class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        M: BFS/DFS , DSU 
        P: Counter of provinces, recrusive function for DFS, visited set to mainatain the cities we already visited, 
            recursive function:
                - check the bounds
                - connected or not 
                - already visited 
                    - return 
                - add in the set
                - recursive call on neighbors

            length of isconnected: n = 3


        """
        total = 0
        self.visited = set()
        n = len(isConnected)

        def dfs(city: int):
            self.visited.add(city)
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in self.visited:
                    dfs(nei)
            return 
            
        for city in range(n):
            if city not in self.visited:
                total += 1
                dfs(city)
                

        return total 

