class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. DFS with memoization
        """
        cache = {}

        def dfs(i: int, j: int) -> int:
            # Base Case -> reached the target point
            if i == (m-1) and j==(n-1):
                return 1
            # Overshoot
            if i >= m or j >= n:
                return 0
            # Cache check
            if (i, j) in cache:
                return cache[(i, j)]
            # Recurrence -> two choices
            # go right -> i, j+1
            # go down -> i+1, j
            cache[(i, j)] = dfs(i, j+1) + dfs(i+1, j)
            return cache[(i, j)]

        return dfs(0, 0)
        """

        # 2. Bottom up 
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
        """

        # 3. Bottom up - Space optimized
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]

            row = newRow

        return row[0]

