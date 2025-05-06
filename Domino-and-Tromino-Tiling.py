class Solution:
    def numTilings(self, n: int) -> int:
        # Value for Modulo
        MOD = 10 ** 9 + 7
        # Cache for func f
        fcache = {}
        # Cache for func p
        pcache = {}


        def p(n):
            # Base Case
            if n == 2:
                return 1
            # Check in cache
            if n in pcache:
                return pcache[n]
            # Regular Case
            pcache[n] = p(n-1) + f(n-2)
            return pcache[n]


        def f(n):
            # Base Case
            if n <= 2:
                return n
            # Check in cache
            if n in fcache:
                return fcache[n]
            # Regular case
            fcache[n] = f(n-1) + f(n-2) + 2 * p(n-1)
            return fcache[n]

        return f(n) % MOD
        

