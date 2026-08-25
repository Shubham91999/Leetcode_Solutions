class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        multiple = k
        i = 2
        while multiple in nums:
            multiple = k * i
            i += 1
        return multiple 


        