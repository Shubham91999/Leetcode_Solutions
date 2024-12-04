class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for i in nums:
            if i in my_set:
                return True
            my_set.add(i)
        return False