class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. BFS with visit set
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # area = 0
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # def bfs(r, c):
        #     q = collections.deque()
        #     q.append((r, c))
        #     visit.add((r, c))
        #     res = 1

        #     while q:
        #         row, col = q.popleft()

        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc
        #             if (nr in range(rows)) and (nc in range(cols)) and grid[nr][nc] == 1 and (nr, nc) not in visit:
        #                 q.append((nr, nc))
        #                 visit.add((nr, nc))
        #                 res += 1
        #     return res


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r, c) not in visit:
        #             area = max(area, bfs(r, c))
        # return area

        # 2. DFS with visit
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0

        def dfs(r, c) -> int:
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visit):
                return 0

            visit.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area



