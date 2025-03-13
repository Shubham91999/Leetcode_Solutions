"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # 1. Recursion
        # def dfs(n, r, c):
        #     # To check base case i.e. all grid elements are same
        #     # Setting allSame flag to True
        #     allSame = True
        #     # Nested loops to access all elements of grid
        #     for i in range(n):
        #         for j in range(n):
        #             # Comparing first grid element with all other
        #             if grid[r][c] != grid[r + i][c + j]:
        #                 # If different element found, setting flag to false
        #                 allSame = False
        #                 break
        #     # After checking all elements if flag is still True, simple create root node with first value with ifLeaf as True
        #     if allSame:
        #         return Node(grid[r][c], True)

        #     # Case: When elements are different
        #     n = n // 2
        #     topleft = dfs(n, r, c) # Since topleft, it will start from (r,c) -> (0,0)
        #     topright = dfs(n, r, c+n) # It will start from first row, mid column -> (r, c+n)
        #     bottomleft = dfs(n, r+n, c) # Mid row, first column -> (r+n, c)
        #     bottomright = dfs(n, r+n, c+n) # Mid row, mid column -> (r+n, c+n)

        #     # Constructing node for second case
        #     return Node(0, False, topleft, topright, bottomleft, bottomright)
        # return dfs(len(grid), 0, 0)

        # 2. Recursion Space Optimized
        leafNodes = {
            0: Node(False, True),
            1: Node(True, True)
        }

        def dfs(n, r, c):
            if n==1:
                return leafNodes[grid[r][c]]

            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c+n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)

            if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val):
                return topleft
            return Node(False, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)




        