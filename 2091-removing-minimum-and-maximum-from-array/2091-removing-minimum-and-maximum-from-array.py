class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        i = min(min_index, max_index)
        j = max(min_index, max_index)

        return min(
            j + 1,              # both from front
            n - i,              # both from back
            i + 1 + n - j       # one from each side
        )