class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. DP: Top-down, recursion with memoization
        """
        m, n = len(text1), len(text2)
        cache = {}

        def dfs(i: int, j: int) -> int:
            # base case: reached the end of any of the strings
            if i == m or j == n:
                return 0
            # cache check
            if (i, j) in cache:
                return cache[(i, j)]

            # recurrence: two choices 
            res = 0
            # current chars matched
            if text1[i] == text2[j]:
                res = 1 + dfs(i+1, j+1)
            # current chars do not match
            else:
                # can skip char from either of the strings
                skip_text1 = dfs(i+1, j)
                skip_text2 = dfs(i, j+1)
                res = max(skip_text1, skip_text2)

            cache[(i, j)] = res
            return res

        return dfs(0, 0)
        """

        # 2. DP: Bottom-up
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
        """

        # 3. DP: Bottom-up, space optimized
        m, n = len(text1), len(text2)
        dp = [0] * (n+1)

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    newDp[j] = 1 + dp[j+1]
                else:
                    newDp[j] = max(dp[j], newDp[j+1])
            dp = newDp

        return dp[0]