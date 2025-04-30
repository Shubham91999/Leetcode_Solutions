class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Brute Force: Checking all rows, columns and squares one by one
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])

        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[col][i] == ".":
        #             continue
        #         if board[col][i] in seen:
        #             return False
        #         seen.add(board[col][i])

        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square // 3) * 3 + i
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True

        # 2. Hash Set One Pass
        cols = defaultdict(set) # Dictionary of hash sets with key as column number
        rows = defaultdict(set)
        squares = defaultdict(set) # Key : (r // 3) , (c // 3)

        for r in range(9): # Hardcoding ranges as the board size is 9
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c]) # Adding number to respective row and column sets
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c]) 
        return True





