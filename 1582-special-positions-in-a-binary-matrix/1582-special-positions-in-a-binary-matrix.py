class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        ROWS, COLS = len(mat), len(mat[0])

        def helper(r: int, c: int) -> int:
            # Special -> 1
            # Not special -> 0

            # loop right
            for i in range(c+1, COLS):
                if mat[r][i] == 1:
                    return 0
            # loop left
            for i in range(c-1, -1, -1):
                if mat[r][i] == 1:
                    return 0
            # loop up 
            for i in range(r-1, -1, -1):
                if mat[i][c] == 1:
                    return 0
            # loop down
            for i in range(r+1, ROWS):
                if mat[i][c] == 1:
                    return 0
            return 1
 


        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    count += helper(r, c)
        return count