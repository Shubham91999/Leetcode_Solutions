class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. Brute Force Approach
        # if not height:
        #     return 0
        # n = len(height)
        # res = 0

        # for i in range(n): 
        #     leftMax = rightMax = height[i]
        #     for j in range(i):  # Traversing elements at left of ith element
        #         leftMax = max(leftMax, height[j])
        #     for j in range(i+1, n):  # Traversing elements at right of ith element
        #         rightMax = max(rightMax, height[j])

        #     res += min(leftMax, rightMax) - height[i]
        # return res

        # 2. Two Pointer
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res        



