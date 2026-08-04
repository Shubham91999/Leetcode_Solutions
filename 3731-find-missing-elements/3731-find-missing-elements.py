class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        lower = min(nums)
        upper = max(nums)
        missing = []
        for i in range(lower, upper+1):
            if i not in numSet:
                missing.append(i)
                
        return missing