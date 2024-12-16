class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        1. Brute Force Approach
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """

        """
        2. Sorting Approach
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        """

        """
        3. Using Hashset
        myset = set()
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
        return False
        """
        
        # 4. Checking HashSet Length with array length
        return len(set(nums)) < len(nums)
