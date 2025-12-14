from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1. DP: Recursion with memoization
        """
        cache = {}
        def dfs(i: int) -> int:
            # base case: reached the last position
            if i >= len(nums) - 1:
                return 0
            # base case: current max capacity 0
            if nums[i] == 0:
                return float('inf')
            # cache check
            if i in cache:
                return cache[i]

            # recurrence: return min from all possible combinations
            minJumps = float('inf')
            for j in range(1, nums[i]+1):
                jumps = 1 + dfs(i+j)
                minJumps = min(minJumps, jumps)
            cache[i] = minJumps
            return minJumps

        return dfs(0)
        """

        # 2. Greedy Approach
        l = r = 0
        res = 0

        while r < (len(nums) - 1):
            farthest = 0
            for i in range(l, r+1):
                cur_max = i + nums[i]
                farthest = max(farthest, cur_max)
            res += 1
            l = r + 1
            r = farthest
        return res


