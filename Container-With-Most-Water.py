class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. Brute Force Approach Nested For loop
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                res = max(res, area)
        return res
        """ 
        # 2. Two Pointer approach
        res = 0 
        l, r = 0, len(height) - 1

        while l < r:
            #area = min(height[l], height[r]) * (r-l)
            res = max(res, min(height[l], height[r]) * (r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res