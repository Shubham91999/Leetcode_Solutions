class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 1. Capture unsurrounded region as "T"
        def capture(r, c):
            if (r not in range(rows) or (c not in range(cols)) or board[r][c]!="O"):
                return
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                capture(nr, nc)

        # Calling capture function on border cell having "O"
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O") and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        # 2. Mark surrounded region as "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3. Mark "T" region back as "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"