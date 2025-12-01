from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1. Brute Force -> Calculating product for each subarray, maintaining max
        # Time: O(2^n), Space: O(1)
        """
        res = nums[0]

        for i in range(len(nums)):
            cur = nums[i]  # Current product initialized by ith (first in current subarray) element
            res = max(res, cur)

            for j in range(i+1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res
        """

        # 2. Sliding window
        # Time: O(n), Space: O(n)
        """
        if len(nums) == 1 and nums[0] == 0:
            return 0

        A = [] # List of subarrays
        cur = [] # maintain current subarray, unitll we hit 0
        res= float('-inf')

        # Separating subarrays, using separator as 0
        for num in nums:
            res = max(res, num) # max positive number as res
            if num == 0:
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur:
            A.append(cur)

        # Checking every subarray for max product
        for sub in A:
            # Finding total negative numbers in current subarray
            # even negs -> migh give max product
            # odd negs -> no max product, remove/shrink subarray to get max product
            negs = 0
            for i in sub:
                if i < 0:
                    negs += 1

            need = negs if negs % 2 == 0 else negs - 1

            # Sliding window to get valid product and subarray
            prod = 1 # Current subarrays product
            negs = 0 # reset negs count
            j = 0  # left boundary

            # i pointer -> right boundary of sliding window
            for i in range(len(sub)):
                prod *= sub[i] # product with current number

                # making sure current subarray valid or not 

                # Number could be -ve or +ve, if -ve increment negs count to check if its matching needs
                if sub[i] < 0:
                    negs += 1
                    # if negs counts is greater than needs, shrink from the left
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j +=1

                # if number is +ve, check boundary to make sure it is a valid subarray
                if j <= i:
                    res = max(res, prod)


        return res
        """

        # 3. Kadane's Algorithm
        res = nums[0] # Initializing with first to handle special case of length 1 and element == 0
        curMin, curMax = 1, 1

        for num in nums:
            # storing curMax to temp, as curMax will be updated and we need for curMin calculation
            temp = num * curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            res = max(res, curMax)
        return res



        

