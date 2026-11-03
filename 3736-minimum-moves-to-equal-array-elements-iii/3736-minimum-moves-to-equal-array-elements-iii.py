class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums_max = max(nums)
        total = 0
        for num in nums:
            total += nums_max - num
        return total