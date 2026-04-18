class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    queue.append((r, c))
                    count += 1

                    while queue:
                        qr, qc = queue.popleft()
                        grid[qr][qc] = '#'

                        for dr, dc in directions:
                            nr, nc = dr + qr, dc + qc
                            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != '1':
                                continue
                            queue.append((nr, nc))
                            grid[nr][nc] = '#'
                            
                        
        return count 