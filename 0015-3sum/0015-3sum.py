"""
[-4, -1, -1, 0, 1, 2, 5]

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sorting the array
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Breaking if first number is positive
            if nums[i] > 0:
                break
            # Skipping duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Two pointer for remaining two numbers
            l, r = i+1, n-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # updating pointers
                    l += 1
                    r -= 1
                    while l < n and nums[l] == nums[l-1]:
                        l += 1

        return res
        




            

            