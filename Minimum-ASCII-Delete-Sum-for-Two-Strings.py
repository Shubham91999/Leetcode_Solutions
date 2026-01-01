class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 1. DP: Top-down, recursion with memoization
        """
        m, n = len(s1), len(s2)
        cache = {}
        def dfs(i: int, j: int) -> int:
            # cache check:
            if (i, j) in cache:
                return cache[(i, j)]
            # base case: reached the end in both strings, that means strings are now equal
            if i >= m and j >= n:
                return 0
            # base case: reached the end in first string
            if i >= m:
                return ord(s2[j]) + dfs(i, j+1)
            # base case: reached the end in second string
            if j >= n:
                return ord(s1[i]) + dfs(i+1, j)

            # recurrence
            # current chars are matching
            if s1[i] == s2[j]:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]

            # if not matching: two choice
            # delete from string1 -> s1[i] + dfs(i+1, j)
            # delete from string2 -> s2[j] + dfs(i, j+1)
            cache[(i, j)] = min(ord(s1[i]) + dfs(i+1, j), ord(s2[j]) + dfs(i, j+1))
            return cache[(i, j)]

        return dfs(0, 0)
        """

        # 2. DP: Bottom-up
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Populate last row
        val = 0
        for i in range(n-1, -1, -1): # i = 3
            val += ord(s2[i])
            dp[m][i] = val

        # Populate last column
        val = 0
        for i in range(m-1, -1, -1):
            val += ord(s1[i])
            dp[i][n] = val

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])

        return dp[0][0]
        """

        # 3. DP: Bottom-up, space optimized
        m, n = len(s1), len(s2)
        dp = [0] * (n+1)

        # populate last row
        val = 0
        for i in range(n-1, -1, -1): # i = 3
            val += ord(s2[i])
            dp[i] = val

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            newDp[n] = dp[n] + ord(s1[i])

            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    newDp[j] = dp[j+1]
                else:
                    newDp[j] = min(ord(s1[i]) + dp[j], ord(s2[j]) + newDp[j+1])

            dp = newDp

        return dp[0]

        