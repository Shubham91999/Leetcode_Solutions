class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(num: int) -> int:
            total = 0
            while num:
                total += (num % 10)
                num = num // 10
            return total

        for i, num in enumerate(nums):
            if i == digit_sum(num):
                return i
        return -1
