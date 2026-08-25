class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        """
        nums = set(nums) # O(n)
        multiple = k
        
        while multiple in nums:
            multiple += k
            
        return multiple 
        """
        seen = [False] * 101

        for num in nums:
            seen[num] = True

        multiple = k

        while multiple <= 100 and seen[multiple]:
            multiple += k

        return multiple


        