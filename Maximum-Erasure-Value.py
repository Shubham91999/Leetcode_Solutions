class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0 
        seen = set()
        result = []
        maxSum = 0
        curSum = 0

        for end in range(n):
            #curSum = 0
            while nums[end] in seen:
                seen.remove(nums[start])
                curSum -= nums[start]
                start += 1
            seen.add(nums[end])
            curSum += nums[end]
            maxSum = max(maxSum, curSum)
            # curSum = 0

        # print(result)
        # print(maxSum)
        return maxSum