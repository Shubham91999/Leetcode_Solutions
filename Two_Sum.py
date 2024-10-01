class Solution(object):
    def twoSum(self, nums, target):
        #Creating a hashmap
        hashmp = {}

        #Storing all list elements in hashmap
        for i, num in enumerate(nums):
            hashmp[num] = i

        #Traversing list to calculate difference between target and element
        for i, num in enumerate(nums):
            if target-num in hashmp and hashmp[target-num] != i:
                return [i, hashmp[target-num]]

        return[]