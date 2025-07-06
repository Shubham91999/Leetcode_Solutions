class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or (r not in range(rows) or (c not in range(cols)) or heights[r][c] < prevHeight)):
                return 
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                dfs(nr, nc, visit, heights[r][c])

        # Running dfs on first and last row, first row -> adding to pac set, last row -> adding to atlantic set
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # Adding heights that can be reached by pacific ocean
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # Adding heights that can be reached by atlantic ocean

        # Running dfs on first and last column, first column -> pacific set, last column -> atlantic set
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        # Checking every position if it exists in both sets
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl: # if in both sets, that means both oceans can be reached by that position
                    res.append([r, c])
        return res

