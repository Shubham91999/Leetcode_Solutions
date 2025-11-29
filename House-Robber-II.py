"""
Two choices at every position:
    - rob current -> next cannot be robbed
    - skip current -> next can be robbed 

Added condition -> circular houses
    - Run calculation leaving first house and again leaving last house
    - return max

"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) == 1:
            return nums[0]

        # Outer function to call calculation on trimmed arrays
        def outer(arr: List[int]) -> int:
            

            cache = {}
            def inner(i: int) -> int:
                # Base Case
                if i >= len(arr):
                    return 0

                # cache check
                if i in cache:
                    return cache[i]

                # recursion
                cache[i] =  max(inner(i+2) + arr[i], inner(i+1))
                return cache[i]

            return inner(0)

        return max(outer(nums[1:]), outer(nums[:-1]))

        