from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> float:
        # Brute Force -> TLE
        # res = float('-inf')

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         if (j - i + 1) % k == 0:
        #             res = max(res, cur_sum)

                
        # return res

        # Optimized brute force
        """
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)

        res = float('-inf')
        for i in range(len(nums)):
            j = i
            while j + k -1 < len(nums):
                subtract = 0 if i == 0 else prefix[i-1]
                res = max(res, prefix[j+k-1] - subtract)
                j += k

        return res
        """

        # PREFIX SUM 

        prefix = [float('inf')] * k
        prefix[0] = 0
        res = float('-inf')
        total = 0

        for i, n in enumerate(nums):
            total += n
            length = i + 1
            prefix_len = length % k
            res = max(res, total - prefix[prefix_len])
            prefix[prefix_len] = min(prefix[prefix_len], total)

        return res

