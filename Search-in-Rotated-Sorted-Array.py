class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Brute Force 
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        """

        # 2. Binary Search Approach
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid

            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1