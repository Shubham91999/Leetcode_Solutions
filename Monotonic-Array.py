class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        increase = True
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                increase = False
                break
        
        if increase:
            return True

        decrease = True
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                decrease = False
                break
        return decrease