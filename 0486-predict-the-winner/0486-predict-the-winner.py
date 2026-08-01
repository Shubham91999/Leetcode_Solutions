class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:


        def maxAdvantage(nums: List[int], i: int, j: int) -> int:
            # Base Case: Last element in nums
            if i == j:
                # Both i and j indices are point to same element, that means its the only number left in array
                return nums[i]

            # No elements left in array
            if i > j:
                return 0

            # Recursive cases: Two Choices
            # Current player takes from left (nums[i])
            left = nums[i] - maxAdvantage(nums, i+1, j)

            # Current player takes from right (nums[j])
            right = nums[j] - maxAdvantage(nums, i, j-1)

            return max(left, right)

        advantage = maxAdvantage(nums, 0, len(nums)-1)

        if advantage >= 0:
            return True
        else:
            return False


        