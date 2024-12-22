class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Brute Force approach with nested for loops
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j]-prices[i])
        return res
        """

        """
        2. Two Pointer approach
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
        """
        # 3. Dynamic Programming approach
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP


