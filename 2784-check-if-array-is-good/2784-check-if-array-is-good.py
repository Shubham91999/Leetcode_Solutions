class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxNums = max(nums)

        freqMap = {i : 0 for i in range(1, maxNums+1)}
        for num in nums:
            freqMap[num] += 1

        # print(freqMap)
        # print(maxNums)

        for num, count in freqMap.items():
            if num == maxNums:
                if count != 2:
                    return False
            else:
                if count != 1:
                    return False
            
        return True

