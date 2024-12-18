class Solution(object):
    def twoSum(self, nums, target):
        """
        1. Nested For Loop
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """

        """
        2. Sorting
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif(cur < target):
                i += 1
            else: 
                j -= 1
        return []

        """

        """"
        3. HashMap Two pass approach
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]] 

        """

        # 4. Hashmap One Pass approach
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i