class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        list1 = [0] * len(nums)
        list1[0] = 1
        for i in range(1, len(nums)):
            list1[i] = nums[i-1] * list1[i-1]
            #print(list1)

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            list1[i] = list1[i] * suffix
            suffix = suffix * nums[i]
        return list1
        """

        """
        1. Brute Force Approach
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res
        """

        """
        2. Floor Division 
        prod, cnt_zero = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                cnt_zero += 1
        if cnt_zero > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if cnt_zero:
                res[i] = 0 if c else prod
            else: 
                res[i] = prod // c
        return res
        """

        """
        3. Prefix Suffix with separate arrays
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]

        for i in range(len(nums)-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res
        """

        #4. Prefix Suffix with constant space
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res 