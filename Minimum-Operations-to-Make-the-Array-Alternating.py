class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Splitting array in two groups: even and odd indices
        even_group = nums[::2]
        odd_group = nums[1::2]

        # Count frequencies for both groups
        even_freq = Counter(even_group)
        odd_freq = Counter(odd_group)

        # Find two most frequent elemenats in those groups
        even_max = even_freq.most_common(2) # Returns first two pairs sorted in descending order
        odd_max = odd_freq.most_common(2)

        # If there are less than two elements in group, padding list with (0,0)
        while len(even_max) < 2:
            even_max.append((0,0))
        while len(odd_max) < 2:
            odd_max.append((0,0))

        # Compute minimum number of changes
        # case 1: Most freq elements in both groups are different
        if even_max[0][0] != odd_max[0][0]:
            # Return sum of changes required in both groups, (no of numbers in group - frequency of max number)
            return (len(even_group) - even_max[0][1] + len(odd_group) - odd_max[0][1])
        else:
            # case 2: Both are same
            result = min(
            (len(even_group) - even_max[0][1]) + (len(odd_group) - odd_max[1][1]),
            (len(even_group) - even_max[1][1]) + (len(odd_group) - odd_max[0][1])
        )
            return result


        