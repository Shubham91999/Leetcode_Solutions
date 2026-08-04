class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lower = min(nums)
        upper = max(nums)
        missing = []
        for i in range(lower, upper+1):
            if i not in nums:
                missing.append(i)
                
        return missing