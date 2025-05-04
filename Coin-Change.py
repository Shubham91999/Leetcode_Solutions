class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. DP Top Down
        # dp = {}

        # def dfs(amount):
        #     if amount in dp:
        #         return dp[amount]

        #     if amount == 0:
        #         return 0

        #     res = float("inf")
        #     for coin in coins:
        #         remaining_amt = amount - coin
        #         if remaining_amt >= 0:
        #             res = min(res, 1 + dfs(remaining_amt))
        #     dp[amount] = res
        #     return dp[amount]
        # minCoins = dfs(amount)
        # if minCoins >= float("inf"):
        #     return -1
        # else:
        #     return minCoins

        # 2. DP Bottom Up
        dp = [amount + 1] * (amount + 1) # Length will be amount+1, we are going from 0.....amount+1
        dp[0] = 0

        for a in range(1, amount+1): # Starting from bottom i.e. amt = 0, amt = 1, ...amt = amount
            for c in coins: # Trying every coin in coins list
                remaining_amt = a - c
                if remaining_amt >= 0:
                    dp[a] = min(dp[a], 1 + dp[remaining_amt])
        return dp[amount] if dp[amount] != amount + 1 else -1

