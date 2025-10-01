class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       # Set
        """
        numSet = set()
        for num in nums:
                if num in numSet:
                    numSet.remove(num)
                else:
                    numSet.add(num)
        return list(numSet)[0]
        """

        # Using XOR operator

        result = 0
        for num in nums:
            result ^= num
        return result