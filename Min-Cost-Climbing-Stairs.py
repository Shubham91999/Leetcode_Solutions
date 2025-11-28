from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. Recursion with memoization
        """
        n = len(cost)
        cache = {}

        def dfs(i: int) -> int:
            # Base Case -> reached the top of the floor
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            cache[i] =  cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        res = min(dfs(0), dfs(1))

        return res
        """

        # 2. Bottom Up
        """
        n = len(cost)  # 3
        dp = [0] * (n + 1)  # [0, 15, 20, 0]
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]

        for i in range(n-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])
        """

        # 3. Bottom up space optimized

        n = len(cost)

        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])


    






