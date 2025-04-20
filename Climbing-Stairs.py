class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Recursion
        # def dfs(i):
                # Checking base case
        #     if i >= n:
        #         return i == n # returns True if we reached the goal (i==n), False represents it overshooted
        #     return dfs(i+1) + dfs(i+2)

        # return dfs(0)

        # 2. DP Top-Down with Memoization
        # Array for caching
        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i==n
        #     if cache[i] != -1: # if present in cache, return value avoiding recalculation
        #         return cache[i]

        #     cache[i]  = dfs(i+1) + dfs(i+2)
        #     return cache[i]
        # return dfs(0)

        # 3. DP Bottom-Up
        # Checking edge case, if n == 0 and 1, return n
        # if n <= 2:
        #     return n
        # # DP array to store number of ways
        # dp = [0] * (n+1)
        # dp[1], dp[2] = 1, 2 # Initializing for last and second last, dp array is built with output from last element to first (reverse order)
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] # Output of current = output of last + output of second last
        # return dp[n] # returning output present at nth index

        # 4. DP Space Optimization
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp
        return one