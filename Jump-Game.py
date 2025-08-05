class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1. Brute Force -> Time: Exponential : O(2^n)
        # def dfs(i):
        #     if i == len(nums)-1:
        #         return True

        #     end = min(len(nums)-1, i+nums[i])
        #     for j in range(i + 1, end + 1):
        #         if dfs(j):
        #             return True
        #     return False
        # return dfs(0)

        # 2. Dp with Memoization
        # cache = {}
        # def dp(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(nums)-1:
        #         return True
        #     if nums[i] == 0:
        #         return False

        #     end = min(len(nums), i+nums[i]+1)
        #     for j in range(i+1, end):
        #         if dp(j):
        #             cache[i] = True
        #             return True
        #     cache[i] = False
        #     return False
        # return dp(0)

        # 3. Greedy Approach
        n = len(nums)
        goal = n-1

        for i in range(n-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


        