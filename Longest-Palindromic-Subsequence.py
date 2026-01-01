class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 1. DP: Top-down, recursion with memoization
        # Reverse the string and use LCS (longest common subsequence) 
        # Using reversed string, ensures longest subsequence is PALINDROMIC
        """
        rev = s[::-1]
        m = n = len(s)
        cache = {}

        def dfs(i: int, j: int) -> int:
            # base case: reached the end of either string
            if i >= m or j >= n:
                return 0
            # cache check
            if (i, j) in cache:
                return cache[(i, j)]

            # recurrence : two choices
            # current chars match
            if s[i] == rev[j]:
                res = 1 + dfs(i+1, j+1)
            # do not match
            else:
                skip1 = dfs(i+1, j)
                skip2 = dfs(i, j+1)
                res = max(skip1, skip2)
            cache[(i, j)] = res
            return res

        return dfs(0, 0)
        """

        # DP: Bottum-up
        """
        rev = s[::-1]
        m = n = len(s)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == rev[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        """

        # Dp: Bottom-up, space optimized
        rev = s[::-1]
        m = n = len(s)
        dp = [0] * (n+1)

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            for j in range(n-1, -1, -1):
                if s[i] == rev[j]:
                    newDp[j] = 1 + dp[j+1]
                else:
                    newDp[j] = max(dp[j], newDp[j+1])
            dp = newDp
        return dp[0]

        # DP: Top-down, two pointer approach, start - end 
        # if matched, update both
        # if not matched, update one pointer with each dfs call
        """
        cache = {}

        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                cache[(i, j)] = dfs(i + 1, j - 1) + 2
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))

            return cache[(i, j)]

        return dfs(0, len(s) - 1)
        """
