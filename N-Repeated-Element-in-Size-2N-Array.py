from typing import List, Optional

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> Optional[int]:
        # 1. Brute Force, Time : O(n), Space : O(n)
        """
        n = len(nums) // 2
        # freq count
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            if cnt == n:
                return num
        """

        # 2. Optimal, window compare 
        # Time: 3 * O(n), Space: O(1)
        for i in range(1, 4):
            for j in range(len(nums) - i):
                if nums[j] == nums[j+i]:
                    return nums[j]
        

        

        