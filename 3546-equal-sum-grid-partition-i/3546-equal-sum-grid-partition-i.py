class Solution:
    def canPartitionGrid(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        # Step 1: Total sum
        total = sum(sum(row) for row in grid)
        
        # If total is odd → cannot split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Step 2: Horizontal cut
        prefix = 0
        for r in range(rows - 1):  # last row cannot be a cut
            prefix += sum(grid[r])
            if prefix == target:
                return True
        
        # Step 3: Vertical cut
        prefix = 0
        for c in range(cols - 1):  # last column cannot be a cut
            col_sum = 0
            for r in range(rows):
                col_sum += grid[r][c]
            
            prefix += col_sum
            if prefix == target:
                return True
        
        return False