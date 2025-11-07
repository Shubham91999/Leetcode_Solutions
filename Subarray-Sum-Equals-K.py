from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force
        # res = 0

        # for i in range(len(nums)):
        #     cur_total = 0
        #     for j in range(i, len(nums)):
        #         cur_total += nums[j]
        #         if cur_total == k:
        #             res += 1
        # return res

        # Hashmap Approach
        prefixSums = { 0: 1}
        res = 0
        curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)

            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)


        return res

