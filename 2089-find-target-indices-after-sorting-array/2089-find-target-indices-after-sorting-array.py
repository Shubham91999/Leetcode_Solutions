class Solution:
    
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        start = sum(1 for num in nums if num < target)
        count = nums.count(target)

        return list(range(start, start + count))