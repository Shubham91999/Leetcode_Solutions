class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 1. Brute Force
        # n = len(ratings)
        # arr = [1] * n # Intializing array of length (ratings) with 1

        # for i in range(n-1):  # Loop 0 to length - 1
        #     if ratings[i] == ratings[i+1]:
        #         continue
            
        #     if ratings[i+1] > ratings[i]: # If element to right is greater than current element
        #         arr[i+1] = arr[i] + 1  # Update right element's arr value, current element's arr value + 1

        #     elif arr[i] == arr[i+1]: # Right element has lower rating
        #         # arr[i+1] = arr[i]
        #         arr[i] += 1
        #         for j in range(i-1, -1, -1): # Back-adjusting the run on left
        #             if ratings[j] > ratings[j+1]: # Right element is greater than left
        #                 if arr[j+1] < arr[j]: # Right elements rating is greater than left one's
        #                     break
        #                 arr[j] += 1 # 
        # return sum(arr)

        # 2. Greedy Approach (Two Pass)
        n = len(ratings)
        arr = [1] * n

        # First pass, left to right
        for i in range(1, n): # Loop starting for 1 to end
            if ratings[i-1] < ratings[i]: 
                arr[i] = arr[i-1] + 1 # All initialized to 1, so no max check required

        # Second pass, right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1) 
            
        return sum(arr)
        

             