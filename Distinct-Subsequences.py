class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 1. DP: Top-Down, recursion with memoization
        """
        cache = {}
        def dfs(i: int, j: int) -> int:
            # base case: reached the end of target string
            # found valid subsequence, return 1
            if j >= len(t):
                return 1
            # base case: reached the end of input string
            # no valid subsequence possible
            if i >= len(s):
                return 0
            # cache check
            if (i, j) in cache:
                return cache[(i, j)]

            # recurrence
            # current chars do not match
            res = dfs(i+1, j)
            # current chars match: two choices
            # use current char in s -> dfs(i+1, j+1)
            # skip current char in s -> dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            cache[(i, j)] = res
            return res
        return dfs(0, 0)
        """
        

        # 2. DP: Bottom-Up
        """
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # populate last column, base case: reached the end of target string
        for i in range(m+1):
            dp[i][n] = 1
        # print(dp)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # do not match 
                dp[i][j] = dp[i+1][j]
                # if match
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        #print(dp)
        return dp[0][0]
        """

        # 3. DP: Bottop-up, space optimized
        m, n = len(s), len(t)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            newDp[n] = 1
            for j in range(n-1, -1, -1):
                # do not match 
                newDp[j] = dp[j]
                # if match
                if s[i] == t[j]:
                    newDp[j] += dp[j+1]
            dp = newDp
        return dp[0]


        

