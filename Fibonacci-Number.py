class Solution:
    def fib(self, n: int) -> int:
        # 1. DP: Top-Down, recursion with memoization
        """
        cache = {}
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return 1
            # cache check
            if i in cache:
                return cache[i]

            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]

        return dfs(n)
        """
        # 2. Bottom-up Dp
        """
        # [0, 1, 1, 2, 3]
        # n = 4
        # 2. Bottom-up
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        """

        # 3. Bottom-up: Space Optimized
        # [0, 1, 1, 2, 3]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        one, two = 0, 1

        for _ in range(n-1):
            temp = two
            two = one + two
            one = temp

        return two


        
 


