from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 1. Brute Force
        # Time: O(m x n)
        """
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    count += 1

        return count
        """

        # 2. Binary Search
        # Time: O(m log n), m -> rows & log n -> binary search
        """
        rows, cols = len(grid), len(grid[0])
        count = 0
        for row in grid:
            left, right = 0, cols - 1
            while left <= right:
                mid = (left+right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (cols - left)
        return count
        """

        # 3. Linear Traversal
        count = 0
        rows, cols = len(grid), len(grid[0])
        currRowNegativeIndex = cols - 1
        for row in grid:
            while currRowNegativeIndex >= 0 and row[currRowNegativeIndex] < 0:
                currRowNegativeIndex -= 1
            count += (cols - currRowNegativeIndex - 1)
        return count
