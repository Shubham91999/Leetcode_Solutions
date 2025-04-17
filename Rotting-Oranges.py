class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # Queue to traverse BFS
        time, fresh = 0, 0 # Counters to maintain time and number of fresh oranges

        # Iterating over the grid to get number of fresh oranges and initialize queue with rotten ones
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # 1 indicates fresh orange
                    fresh += 1
                if grid[r][c] == 2: # 2 indicates rotten orange
                    q.append([r, c])  # Appending coordinates of rotten oranges in queue
                
        # Looping till queue becomes empty or number of fresh oranges becomes 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):  # In each iteration, all present queue elements are visited
                r, c = q.popleft()  
                for dr, dc in directions: # Adding neighbors for current orange based on directions
                    row = r + dr
                    col = c + dc
                    # Checking if newly calculated indices are inbounds and it is a fresh orange
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1



            
 