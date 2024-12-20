class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. Brute force 
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
        """

        """
        2. Sorting
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)

        return res
        """

        """
        3. Hashset
        mySet = set(nums)
        longest = 0

        for num in mySet:
            if (num-1) not in mySet:
                length = 1
                while(num + length) in mySet:
                    length += 1
                longest = max(length, longest)
        return longest
        """

        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1] + mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
                res = max(res, mp[num])
        return res

