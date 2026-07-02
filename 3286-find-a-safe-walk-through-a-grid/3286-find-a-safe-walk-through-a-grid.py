class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dis = [[float("inf")] * n for _ in range(m)]

        q = deque()
        q.appendleft((0, 0))
        dis[0][0] = grid[0][0]

        while q:
            cx, cy = q.popleft()
            # the first time it leaves the queue, the shortest distance is guaranteed
            if cx == m - 1 and cy == n - 1:
                return True

            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                cost = dis[cx][cy] + grid[nx][ny]
                # pruning: the new distance does not meet health requirements
                if cost >= health:
                    continue

                if cost < dis[nx][ny]:
                    dis[nx][ny] = cost
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))

        return False