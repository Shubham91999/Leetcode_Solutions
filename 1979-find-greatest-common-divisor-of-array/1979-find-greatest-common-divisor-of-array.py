class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums) 
        for i in range(smallest, 1, -1):
            if smallest % i == 0 and largest % i == 0:
                return i
        return 1
        