class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 1. Recursion
        """
        def dfs(i: int, j: int) -> int:
            # Base Case -> reached end of target string
            if j == len(t):
                return 1
            # Reached end of input string
            if i == len(s):
                return 0

            # Recurrence
            # Exclude
            res = dfs(i+1, j)
            # Include
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            
            return res
        return dfs(0, 0)
        """

        # 2. Recursion with memoization
        """
        cache = {}
        def dfs(i: int, j: int) -> int:
            # Base Case -> reached end of target string
            if j == len(t):
                return 1
            # Reached end of input string
            if i == len(s):
                return 0
            # Cache check
            if (i, j) in cache:
                return cache[(i, j)]

            # Recurrence
            # Exclude
            res = dfs(i+1, j)
            # Include
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            cache[(i, j)] = res
            return res
        return dfs(0, 0)
        """

        # 3. Bottom-up: Dp matrix 
        """
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # Last column set to 1
        for i in range(m+1):
            dp[i][n] = 1

        # Matrix population
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j] # Down
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]
        """

        # 4. Bottom-up : space optimized
        m, n = len(s), len(t)
        dp = [0] * (n+1)
        # Last set to 1
        dp[n] = 1

        # Matrix population
        for i in range(m-1, -1, -1):
            nextDp = [0] * (n+1)
            nextDp[n] = 1
            for j in range(n-1, -1, -1):
                nextDp[j] = dp[j] # Down
                if s[i] == t[j]:
                    nextDp[j] += dp[j+1]
            dp = nextDp
        return dp[0]

        


