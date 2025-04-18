class Solution:
    def threeSum(self, numbers: List[List[int]]) -> List[int]:
        # 1. Brute Force: Sort and nested loop for finding pair
        # res = set()
        # numbers.sort()
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         for k in range(j+1, len(numbers)):
        #             if numbers[i] + numbers[j] + numbers[k] == 0:
        #                 temp = [numbers[i], numbers[j], numbers[k]]
        #                 res.add(tuple(temp))
        # return [list(i) for i in res]

        # 2. Two Pointer: Optimal Space
        res = []
        numbers.sort() # Sorted array is required 

        for i, a in enumerate(numbers): # Looping over every number in nums array

            # Optimization by eliminating further checks, 
            # when a is positive, it means b -> nums[l] and c -> nums[r] are going to be positive, addition of three positive numbers can't be 0
            if a > 0:
                break

            # If we get same value as before, we wont reuse, continue to next iteration
            if i > 0 and a == numbers[i-1]:
                continue

            # Two pointer solution used for two sum 
            l, r = i+1, len(numbers) - 1  # Left initialized at current number a i.e. numbers[i] + 1
            while l < r:
                threeSum = a + numbers[l] + numbers[r]
                if threeSum > 0: # If sum of all three is greater then 0
                    r -= 1
                elif threeSum < 0:  # Sum less than 0
                    l += 1
                else:  # Sum == 0, we got pair
                    res.append([a, numbers[l], numbers[r]])
                    # Updating l and r
                    l += 1  
                    r -= 1
                    while numbers[l] == numbers[l-1] and l < r: # Updating left till we pass the repetative elements
                        l += 1
        return res

       