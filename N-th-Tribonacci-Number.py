class Solution:
    def tribonacci(self, n: int) -> int:
        # 1. DP: Top-Down, recursion with memoization
        """
        cache = {}
        def dfs(i: int) -> int:
            # base case
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            # cache check
            if i in cache:
                return cache[i]
            
            cache[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return cache[i]

        return dfs(n)
        """

        # 2. DP: Bottom-up
        # [0, 1, 1, 2, 4, 7]
        """
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        dp = [0] * (n+1)
        dp[1] = dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
        """

        # 3. Bottom-up: Space optimized
        # [0, 1, 1, 2, 4, 7]
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        one, two, three = 0, 1, 1
        for _ in range(n-2):
            temp = three
            three = one + two + three
            one = two
            two = temp
        return three

