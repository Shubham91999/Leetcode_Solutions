"""
@params: nums array, k -> number of integers in one subarray, x -> top most frequent elements
@returns: array of integers

# Edge cases:
    - Null array
    - Array with all elements as 0
    - Values of k and x -> 0

    To be considered for every subarray
    - Length of array less than x distinct elements

Algo:
    - Initialize freq map for k elements
    - Two pointers to create furhter subarray of k elements
    - Populate heap with negatives
    - pop top x freq 
    - calculate current sum
    - append current sum to result array
    - return result array

"""

from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []

        freqMap = defaultdict(int)
        for i in range(k):
            freqMap[nums[i]] += 1

        l, r = 0, k

        while r <= len(nums):
            curSum = 0
            curArray = []

            for val, cnt in freqMap.items():
                curArray.append([-cnt, -val])

            heapq.heapify(curArray)
            s = x

            while s and curArray:
                cnt, val = heapq.heappop(curArray)
                curSum += abs(val * cnt)
                s -= 1

            result.append(curSum)

            if r == len(nums):
                break

            freqMap[nums[l]] -= 1
            if freqMap[nums[l]] == 0:
                del freqMap[nums[l]]
            
            freqMap[nums[r]] += 1

            l += 1
            r += 1

        return result



                



