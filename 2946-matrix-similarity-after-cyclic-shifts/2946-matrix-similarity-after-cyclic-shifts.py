class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        ROWS, COLS = len(mat), len(mat[0])
        k %= COLS

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] != mat[r][(c+k)%COLS]:
                    return False

        return True