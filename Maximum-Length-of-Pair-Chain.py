from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 1. DP: Top-down, recursion with memoization
        """
        pairs.sort()
        cache = {}
        
        def dfs(i: int, prev_end: int) -> int:
            # base case: reached the end of pairs array
            if i >= len(pairs):
                return 0
            # cache check
            if (i, prev_end) in cache:
                return cache[(i, prev_end)]
            
            # recurrence: two choices
            # do no choose current pair
            res = dfs(i+1, prev_end)

            # choose current pair
            if pairs[i][0] > prev_end:
                res = max(res, 1 + dfs(i+1, pairs[i][1]))

            cache[(i, prev_end)] = res
            return res

        return dfs(0, float('-inf'))
        """

        # 2. DP: Bottom-up 
        """
        n = len(pairs)
        pairs.sort()

        dp = [1] * n
        ans = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans
        """

        # 3. Greedy
        # Sort pairs in ascending order based on the second element.
        pairs.sort(key=lambda x: x[1])

        curr = float('-inf') 
        ans = 0

        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans