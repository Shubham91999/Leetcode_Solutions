class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute Force: Nested Loops
        # n = len(nums)
        # res = nums[0] # Track max sum
        # for i in range(n):
        #     cur = 0
        #     for j in range(i, n):
        #         cur += nums[j]
        #         res = max(res, cur)
        # return res

        # 2. Dynamic Programming Space Optimized
        # dp = [x for x in nums]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i]+dp[i-1])
        # return max(dp)

        # 3. Kadane's Algorithm
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum
         
        