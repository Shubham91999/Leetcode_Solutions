class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Brute Force Sorting
        # nums3 = nums1 + nums2
        # nums3.sort()
        # n = len(nums3)
        # if n % 2 == 1:
        #     return nums3[n//2]
        # else:
        #     return (nums3[n//2-1] + nums3[n//2]) / 2.0

        # 2. Two Pointer with no extra space
        # len1, len2 = len(nums1), len(nums2)
        # i, j = 0, 0
        # median1 = median2 = 0

        # for count in range((len1+len2)//2 + 1):
        #     median2 = median1 
        #     if i < len1 and j < len2:
        #         if nums1[i] > nums2[j]:
        #             median1 = nums2[j]
        #             j += 1
        #         else:
        #             median1 = nums1[i]
        #             i += 1
        #     elif i < len1:
        #         median1 = nums1[i]
        #         i += 1
        #     else:
        #         median1 = nums2[j]
        #         j += 1
        # if (len1 + len2) % 2 == 1:
        #     return median1
        # else:
        #     return (median1 + median2) / 2.0
        
        # 3. Binary Search Optimal solution
        A, B = nums1, nums2
        total = len(nums1) + len(nums2) # Getting total length and half 
        half =  total // 2  

        # We are ginna run binary search on minimum length array
        if len(B) < len(A): # if B is smaller in size, swapping the arrays
            A, B = B, A  # A will always point to min array

        # Running binary search on A
        l, r = 0, len(A)-1

        while True:
            i = (l + r) // 2  # i -> middle of array A
            j = half - i - 2  # j -> middle of array B     

            # Values to determine the median
            # i, i+1, j, j+1 indices could go out of bounds, so assigning after checking  
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            # Checking our partition is correct or not
            if Aleft <= Bright and Bleft <= Aright:
                # odd number of elements (total)
                if total % 2:
                    return min(Aright, Bright)
                # even number of elements (total)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # We didnt find median, either of the array is way big than other
            # 
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



