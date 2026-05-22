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
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # If we are in left sorted portion
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1