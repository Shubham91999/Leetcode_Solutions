from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 1. DP: Top-down
        """
        cache = {}
        n = len(arr)
        def dfs(i: int) -> int:
            # base case: reached the end of arr
            if i >= len(arr):
                return 0
            # cache check
            if i in cache:
                return cache[i]

            LIS = 1
            for j in range(i+1, n):
                if arr[i] + difference == arr[j]:
                    LIS = max(LIS, 1 + dfs(j))
            cache[i] = LIS
            return LIS

        res = 0 
        for i in range(n):
            res = max(res, dfs(i))
        return res
        """

        # 2. Hashmap DP
        dp = {}
        best = 0

        for x in arr:
            dp[x] = dp.get(x - difference, 0) + 1
            best = max(best, dp[x])
        return best 


