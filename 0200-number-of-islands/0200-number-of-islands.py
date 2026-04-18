class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    count += 1
                    queue = deque([(r, c)])  # ✅ fresh queue per island
                    grid[r][c] = '#'        # ✅ mark before appending

                    while queue:
                        cr, cc = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != '1':
                                continue
                            grid[nr][nc] = '#'  # ✅ mark when appending, not popping
                            queue.append((nr, nc))

        return count