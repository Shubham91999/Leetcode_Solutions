class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. Brute Force : Iteration
        # res = [[]]
        # for num in nums:
        #     new_subsets = []
        #     for subset in res:
        #         new_subset = subset + [num]
        #         new_subsets.append(new_subset)
        #     res.extend(new_subsets)
        # return res

        # 2. Backtracking: Include/Don't Include
        res = []
        subsets = []

        def dfs(i):
            if i >= len(nums):  # Base case: i exceeds the length of nums array, subset's length should be less than arrays length 
                res.append(subsets.copy()) # Lists are mutable in python, copy() will ensure, ref of immutable (list not updated in code)
                return 

            # Decision to INCLUDE
            subsets.append(nums[i])
            dfs(i+1)

            # Not to include
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res


