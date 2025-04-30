class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # Getting number of rows and columns
        path = set()  # Mentioned, we may not used same char more than once

        def dfs(r, c, i): # Nested function to pass arguments as required
            if i == len(word): # If we reach end of the word, it means we found all chars in word
                return True

            # Checking three conditions:
            # 1. Updated values of r and c are in bounds
            # 2. Current char from word is matching with current char from board
            # 3. Char at index (r,c) is already visited
            if r not in range(ROWS) or c not in range(COLS) or word[i] != board[r][c] or (r, c) in path:
                return False
            # Adding it in set path, to avoid visiting again
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            # Removing from path after processing
            path.remove((r,c))
            return res
        # Running dfs for all the chars in matrix
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

