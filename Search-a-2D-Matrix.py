class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Searching correct row
        top, bot = 0, rows - 1
        
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # If bot became lesser than top, it means we didn't find target in rows
        if not top <= bot:
            return False
        
        # Searching in row
        row = (top+bot) // 2
        l, r = 0, cols - 1
        
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False