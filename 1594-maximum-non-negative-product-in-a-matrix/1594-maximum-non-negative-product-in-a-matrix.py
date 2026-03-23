class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ROWS, COLS = len(grid), len(grid[0])

        # dp arrays
        dp_max = [[0] * COLS for _ in range(ROWS)]
        dp_min = [[0] * COLS for _ in range(ROWS)]

        # base case
        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]

        # fill first row
        for c in range(1, COLS):
            val = grid[0][c]
            dp_max[0][c] = dp_max[0][c-1] * val
            dp_min[0][c] = dp_min[0][c-1] * val

        # fill first column
        for r in range(1, ROWS):
            val = grid[r][0]
            dp_max[r][0] = dp_max[r-1][0] * val
            dp_min[r][0] = dp_min[r-1][0] * val

        # fill rest of grid
        for r in range(1, ROWS):
            for c in range(1, COLS):
                val = grid[r][c]

                candidates = [
                    dp_max[r-1][c] * val,
                    dp_min[r-1][c] * val,
                    dp_max[r][c-1] * val,
                    dp_min[r][c-1] * val
                ]

                dp_max[r][c] = max(candidates)
                dp_min[r][c] = min(candidates)

        result = dp_max[ROWS-1][COLS-1]

        if result < 0:
            return -1
        return result % MOD