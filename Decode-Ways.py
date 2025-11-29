class Solution:
    def numDecodings(self, s: str) -> int:
        # Cache for memoization
        cache = {}

        def dfs(i: int) -> int:
            # Base cases
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            # Cache check
            if i in cache:
                return cache[i]
            # Recursion
            # Decoding using only one char
            res = dfs(i+1)
            # Decoding using two chars
            # checking valid or not -> two conditions 
            # should be in bounds
            # number formed by two chars should be inbetween 10 - 26
            if ((i + 1) < len(s)) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                res += dfs(i+2)

            cache[i] = res
            return res

        # Calling dfs
        count = dfs(0)
        # Return result
        return count 