class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> int:
            # Base checks
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            sum_values = grid[r][c]
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                sum_values += dfs(nr, nc)
            return sum_values


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0 and (r, c) not in visited:
                    cur_sum = dfs(r, c)
                    if cur_sum % k == 0:
                        total += 1

        return total 