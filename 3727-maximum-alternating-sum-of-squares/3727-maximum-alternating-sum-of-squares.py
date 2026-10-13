
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(n * n for n in nums)
        l = 0
        r = len(squares) - 1
        total = 0

        while l < r:
            total += squares[r] - squares[l]
            l += 1
            r -= 1

        if l == r:
            total += squares[r]

        return total
