from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Brute Force: Recursion
        """
        def dfs(i: int, curSum: int) -> int:
            # Base Case -> reached end i.e. used all numbers from i/p array
            if i >= len(nums):
                return curSum == target

            # Recursive calls
            return dfs(i+1, curSum + nums[i]) + dfs(i+1, curSum - nums[i])

        return dfs(0, 0)
        """

        # Top-Down: Recursion with memoization
        """
        cache = {}
        def dfs(i: int, curSum: int) -> int:
            # Base Case -> reached end i.e. used all numbers from i/p array
            if i >= len(nums):
                return curSum == target

            # Cache check
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            # Recursive calls
            cache[(i, curSum)] = dfs(i+1, curSum + nums[i]) + dfs(i+1, curSum - nums[i])
            return cache[(i, curSum)]

        return dfs(0, 0)
        """

        # Bottom-up: DP matrix population
        """
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        # dp[numbers used][current sum] = [possible ways]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count

        return dp[n][target]
        """

        # Bottom-up: space optimized
        dp = defaultdict(int)
        dp[0] = 1
        n = len(nums)
        for i in range(n):
            newDp = defaultdict(int)
            for total, count in dp.items():
                newDp[total + nums[i]] += count
                newDp[total - nums[i]] += count
            dp = newDp
        return dp[target]



