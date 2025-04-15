class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # 1. Sorting O(n log n)
        # Edge case
        # if k == 1:
        #     return 0

        # # Array to store cost of each split
        # splits = [weights[i] + weights[i+1] for i in range(len(weights)-1)]

        # splits.sort()   # Sorting splits array to get min and max split cost

        # i = k - 1  # Considering number of splits

        # max_score = weights[0] + weights[-1] + sum(splits[-i:]) # Sum of first, last element of weights and last k elements in splits array
        # min_score = weights[0] + weights[-1] + sum(splits[:i])  # Sum of first, last element of weights and first k in splits

        # return max_score - min_score # Returning diff of max and min score

        # 2. Heap  O(n log k)
        # Edge case
        if k == 1:
            return 0

        splits = [weights[i] + weights[i+1] for i in range(len(weights)-1)]

        max_score = heapq.nlargest(k-1, splits) # heap method to get k-1 largest from splits
        min_score = heapq.nsmallest(k-1, splits) # heap method to get k-1 smallest from splits

        return sum(max_score) - sum(min_score) # Not considerig first and last element, as anyway we are adding them on both sides


