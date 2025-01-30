class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        if target < min(nums):
            return 0
        elif target > max(nums):
            return r + 1
            
        while l <= r:
            mid = (l+r) // 2
            print(f"Left {l}")
            print(f"Right {r}")

            print(f"Mid {mid}")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
                
        return l
            
        # # Lower and upper bounds
        # start = 0
        # end = len(nums) - 1
    
        # # Traverse the search space
        # while start<= end:
    
        #     mid =(start + end)//2
    
        #     if nums[mid] == target:
        #         return mid
    
        #     elif nums[mid] < target:
        #         start = mid + 1
        #     else:
        #         end = mid-1
    
        # # Return the insert position
        # return end + 1 