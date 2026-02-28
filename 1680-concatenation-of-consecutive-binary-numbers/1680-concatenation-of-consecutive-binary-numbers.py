class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = ''

        for i in range(1, n+1):
            res += bin(i)[2:]

        return floor(int(res, 2) % MOD)