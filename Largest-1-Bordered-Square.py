from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        L = [g[:] for g in grid]  # Prefix array for letf to right
        R = [g[:] for g in grid]  # Right to left
        A = [g[:] for g in grid]  # Top to bottom
        B = [g[:] for g in grid]  # Bottom to top

        # Populating the prefix arrays
        for i in range(len(grid)):
            for j in range(len(grid[0])): # Populating left to right consecutive 1's sum array
                if L[i][j]:
                    L[i][j] += L[i][j-1]

            for j in range(len(grid[0])-2, -1, -1): # Right to left
                if R[i][j]:
                    R[i][j] += R[i][j+1]

        for j in range(len(grid[0])):
            for i in range(1, len(grid)): # Top to Bottom
                if A[i][j]:
                    A[i][j] += A[i-1][j]

            for i in range(len(grid)-2, -1, -1): # Bottom to Top
                if B[i][j]:
                    B[i][j] += B[i+1][j]

        LS = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(min(L[i][j], A[i][j])): # For every pair of (i, j), min value from Left and Above, starting from 0 to min value
                    if min(R[i-k][j-k], B[i-k][j-k]) >= k: # Check if the min value from Right and Bottom is greater than or equal to k from range 0 to min of left and above
                        LS = max(LS, (k+1)**2)
        return LS

