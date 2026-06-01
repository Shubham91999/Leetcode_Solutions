class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return sum(cost)

        cost = sorted(cost, reverse=True) # [2, 2, 5, 6, 7, 9]
        total = 0

        for i in range(n):
            if (i + 1) % 3 == 0:
                continue
            total += cost[i]

        return total
            


