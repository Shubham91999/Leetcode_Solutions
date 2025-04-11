class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. Breadth First Search
        # if not grid:  # Edge case, Null grid
        #     return 0

        # rows = len(grid) # Number of rows -> lenght of grid
        # columns = len(grid[0]) # Number of columns -> Length of first list present in matrix

        # visit = set()  # Set to track visited nodes
        # islands = 0     # Count of islands

        # def bfs(r, c):
        #     q = collections.deque()  # BFS uses queue
        #     visit.add((r, c))  # Add it to already visited
        #     q.append((r, c)) # Appending in queue for bfs traversal
            
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0],  # Down
        #                         [-1, 0], # Up
        #                         [0, 1],  # Right
        #                         [0, -1]  # Left
        #                         ]

        #         for dr, dc in directions:
        #             r = row + dr # Getting new row & column value to visit neighbors
        #             c = col + dc
                    
        #             if r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r, c) not in visit:
        #                 q.append((r, c))
        #                 visit.add((r, c))



        # for r in range(rows):     # Traversing each element in grid
        #     for c in range(columns):
        #         if grid[r][c] == "1" and (r, c) not in visit:   # If the current node is 1 and is not already visited
        #             bfs(r, c)  # Run bfs on it, to check its neighbors
        #             islands += 1 # Increment count of islands
        # return islands   # Return the result i.e. islands

        # 2. Iterative DFS with inplace modifications
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == "1":
                        q.append((r, c))
                        grid[r][c] = "0"

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands 
                    



        