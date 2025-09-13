class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # numSet = set()
        # for num in nums:
        #     if num in numSet:
        #         return num
        #     numSet.add(num)

        # Using slow and fast pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow 

        # Time: O(n), Space: O(1)