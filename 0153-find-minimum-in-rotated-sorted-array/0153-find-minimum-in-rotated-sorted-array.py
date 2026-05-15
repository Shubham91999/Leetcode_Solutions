class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Binary Search
        """
        res = nums[0]
        l ,r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
        """

        # 2. Binary Search (Lower Bound)
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else: 
                l = m + 1
        return nums[l]