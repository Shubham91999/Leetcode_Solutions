"""
@params
m -> rows
n -> columns
guards -> list of coordinates -> starting point for bfs/dfs
walls -> list of coordinates -> obstruction for guards -> stop bfs/dfs

@return
int -> number of cells that are not guarded

Plan:
    - add guard points in queue
    - start bfs for guard point
        - traverse in four directions -> (0, 1), (0, -1), (1, 0), (-1, 0)
        - check for bounds and wall
            - if not valid, do not mark and stop traversal
            - if valid, mark as guarded (True)
    - traverse all cells again and increment count
    - return count
"""
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize grid: 0 = unoccupied, 1 = wall/guard, 2 = guarded
        grid = [[0] * n for _ in range(m)]
        
        # Place guards and walls in the grid
        for r, c in guards:
            grid[r][c] = 1  # Guard
        for r, c in walls:
            grid[r][c] = 1  # Wall
        
        # Directions for cardinal movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Mark cells guarded by the guards
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:  # Stop at a wall or another guard
                        break
                    if grid[nr][nc] == 0:  # Mark as guarded
                        grid[nr][nc] = 2
                    nr += dr
                    nc += dc
        
        # Count unoccupied and unguarded cells
        unguarded_count = sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)
        
        return unguarded_count
