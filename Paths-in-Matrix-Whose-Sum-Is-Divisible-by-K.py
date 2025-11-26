from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        cache = {}
        

        def dfs(r: int, c: int, cur_mod: int):
            # Base Case -> reached the bottom-right
            if r == (m-1) and c == (n-1):
                if cur_mod % k == 0:
                    return 1
                else:
                    return 0

            # Check in cache
            if (r, c, cur_mod) in cache:
                return cache[(r, c, cur_mod)]

            total = 0

            # Move DOWN
            if r + 1 < m:
                new_mod = (cur_mod + grid[r+1][c]) % k
                total += dfs(r + 1, c, new_mod)

            # Move RIGHT
            if c + 1 < n:
                new_mod = (cur_mod + grid[r][c+1]) % k
                total += dfs(r, c + 1, new_mod)

            total %= MOD
            cache[(r, c, cur_mod)] = total
            return total


        return dfs(0, 0 , grid[0][0] % k)

        