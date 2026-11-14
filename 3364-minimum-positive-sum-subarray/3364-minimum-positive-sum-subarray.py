

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minimum = float('inf')

        for length in range(l, r+1):
            total = 0
            for i in range(n):
                total += nums[i]
                if i >= length:
                    total -= nums[i - length]
                if i >= length - 1 and 0 < total < minimum:
                    minimum = total
        return minimum if minimum != float('inf') else -1