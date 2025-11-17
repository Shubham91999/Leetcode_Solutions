from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l, r = -1, 0

        while r < len(nums):
            if nums[r] == 1:
                if l != -1 and (r-l-1) < k:
                    return False
                l = r

            r += 1
            
        return True
