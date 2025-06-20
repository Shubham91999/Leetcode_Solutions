class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
            return 

        province = 0  # To keep the count of provinces
        self.visited = set() # Avoid repition
        n = len(isConnected)  # Size of given matrix
        for i in range(n):
            if i not in self.visited:
                province += 1
                dfs(i)

        return province
