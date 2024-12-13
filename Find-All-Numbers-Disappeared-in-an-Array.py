class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        store = set(range(1, n + 1))
        
        for num in nums:
            store.discard(num)
        
        return list(store)