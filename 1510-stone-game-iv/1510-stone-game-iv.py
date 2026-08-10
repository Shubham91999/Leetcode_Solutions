class Solution:
    MAX = 10**5
    dp = [False] * (MAX + 1)

    for i in range(MAX + 1):
        if dp[i]: continue

        for j in range(1, isqrt(MAX - i) + 1):
            dp[i + j**2] = True

    def winnerSquareGame(self, n: int) -> bool:
        return self.dp[n]