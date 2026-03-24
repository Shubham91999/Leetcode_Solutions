"""
- Get all the matrix elements in array
- Calculate prefix
- Calculate suffix
- Product array except itself
- Mod values by 12345
- Rebuild matrix from the product array
"""

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        MOD = 12345

        nums = []

        for r in range(ROWS):
            for c in range(COLS):
                nums.append(grid[r][c])
        # print(f"Rows: {ROWS}, Columns: {COLS}")
        # print(nums)

        n = len(nums)
        prefix = [1 for i in range(n)]
        suffix = [1 for i in range(n)]

        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = (prefix[i-1] * nums[i-1]) % MOD

        suffix[n-1] = 1
        for i in range(n-2, -1, -1):
            suffix[i] = (suffix[i+1] * nums[i+1]) % MOD

        # print(f"Prefix array: {prefix}")
        # print(f"Suffix array: {suffix}")

        res = [1 for i in range(n)]
        for i in range(n):
            res[i] = (prefix[i] * suffix[i]) % MOD
        
        # print(f"Result array: {res}")

        mat = [[1 for i in range(COLS)] for j in range(ROWS)]
        # print(mat)

        index = -1

        for r in range(ROWS):
            for c in range(COLS):
                index += 1
                mat[r][c] *= (res[index] % MOD)

        #print(mat)
        return mat
        