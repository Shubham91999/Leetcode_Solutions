class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. Recursion
        # m, n = len(word1), len(word2)
        # def dfs(i, j):
        #     # Checking if any of the words empty
        #     if i == m: # Length of word1 m is equal to 0, number of operation required will be equal to length of word2
        #         return n-j

        #     if j == n: # If word2 length is 0
        #         return m - i

        #     if word1[i] == word2[j]:
        #         return dfs(i+1, j+1) # Current char in both words is matching, so no operations required, simply calling dfs on next indices

        #     # If char not same, try all possible operations and return min
        #     delete_cost = dfs(i+1, j) # Deleting from word1
        #     insert_cost = dfs(i, j+1) # Inserting in word2
        #     replace_cost = dfs(i+1, j+1) # Replacing word1 -> word2

        #     res = min(delete_cost, insert_cost, replace_cost) # Returning min cost 
        #     return res+1 # Account for the one edit we just performed
        # return dfs(0,0)

        # 2. Dynamic Programming (Top Down)
        """
        m, n = len(word1), len(word2)
        cache = {}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == m:
                return n - j
            if j == n:
                return m - i

            if word1[i] == word2[j]:
                return dfs(i+1, j+1)

            delete_cost = dfs(i+1, j)
            insert_cost = dfs(i, j+1)
            replace_cost = dfs(i+1, j+1)
            res = 1 + min(delete_cost, insert_cost, replace_cost)
            cache[(i, j)] = res
            return res
        return dfs(0, 0)
        """

        # 3. DP: Bottom-up 
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # setting base case values
        # last row
        for i in range(n+1):
            dp[m][i] = n - i
        # last column 
        for i in range(m+1):
            dp[i][n] = m - i

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # if char matches
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]
        """

        # 4. Bottom-up, space optimized
        m, n = len(word1), len(word2)
        dp = [0] * (n+1)

        for i in range(n+1):
            dp[i] = n - i

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            newDp[n] = m - i
            for j in range(n-1, -1, -1):
                # if char matches
                if word1[i] == word2[j]:
                    newDp[j] = dp[j+1]
                else:
                    newDp[j] = 1 + min(dp[j], dp[j+1], newDp[j+1])
            dp = newDp
        return dp[0]        

