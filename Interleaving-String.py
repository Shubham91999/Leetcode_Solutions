class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 1. Brute Force - Recursion
        """
        def dfs(i: int, j: int) -> bool:
            # Base Case -> reached end of both strings
            if i == len(s1) and j == len(s2):
                return True
            
            # Recurrence
            # Two choices
            #   - Char from s1 matched, increment index at s1 -> i+1, j
            #   - Char from s2 matched, increment index at s2 -> i, j+1

            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True

            return False
        
        return dfs(0, 0)
        """

        # 2. DP Top-Down: Recursion with memoization
        """
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def dfs(i: int, j: int) -> bool:
            # Base Case -> reached end of both strings
            if i == len(s1) and j == len(s2):
                return True
            # Cache check
            if (i, j) in cache:
                return cache[(i, j)]

            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                cache[(i, j)] = True
                return True
            
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                cache[(i, j)] = True
                return True

            cache[(i, j)] = False
            return False
        
        return dfs(0, 0)
        """

        # 3. Bottom-Up : DP Matrix population
        m, n, r = len(s1), len(s2), len(s3)

        if m + n != r:
            return False
        # Dp matrix initialized with False
        dp = [[False] * (n+1) for _ in range(m+1)]
        # Simultaing base case -> reached end of both strings
        dp[m][n] = True

        # Calculating dp matrix in reverse manner
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
            
                if j < n and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]
        
                



