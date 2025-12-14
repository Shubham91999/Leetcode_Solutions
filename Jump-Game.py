from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Brute Force : Recursion
        """
        def dfs(i: int) -> bool:
            # base case: reached the last position
            if i == len(nums) - 1:
                return True
            # base case: overshoot
            if i >= len(nums):
                return False

            # recurrence
            for j in range(1, nums[i]+1):
                next_index = i + j
                if dfs(next_index):
                    return True

            return False
        return dfs(0)
        """

        # 2. DP: Recursion with memoization
        """
        cache = {}
        def dfs(i: int) -> bool:
            # base case: reached the last position
            if i == len(nums) - 1:
                return True
            # base case: overshoot
            if i >= len(nums):
                return False
            # cache check
            if i in cache:
                return cache[i]

            # recurrence
            for j in range(1, nums[i]+1):
                next_index = i + j
                if dfs(next_index):
                    cache[i] = True
                    return True

            cache[i] = False
            return False
        return dfs(0)
        """

        # 3. Greedy approach
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            cur_max = i + nums[i]
            if cur_max >= goal:
                goal = i
        return goal == 0