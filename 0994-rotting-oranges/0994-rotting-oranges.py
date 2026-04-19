class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        queue = deque()
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        minutes = 0
        while queue:
            for i in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count -= 1
                        queue.append((nr, nc))

            minutes += 1

        if count == 0:
            return max(0, minutes - 1)
        else:
            return -1
                