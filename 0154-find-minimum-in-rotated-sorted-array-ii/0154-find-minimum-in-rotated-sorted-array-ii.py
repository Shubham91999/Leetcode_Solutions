class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Min must be in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Min is in the left half (mid could be the min)
                right = mid
            else:
                # nums[mid] == nums[right]: can't tell which side, shrink right
                right -= 1

        return nums[left]