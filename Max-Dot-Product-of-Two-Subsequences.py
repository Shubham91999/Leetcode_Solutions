from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # 1. DP: Top-Down
        """
        cache = {}

        def dfs(i: int, j: int, picked: bool) -> int:
            # base case
            if i >= len(nums1) or j >= len(nums2):
                return 0 if picked else float('-inf')
            # cache check
            if (i, j, picked) in cache:
                return cache[(i, j, picked)]

            # recurrence: three choices 
            # 1. choose current pair i.e. numbers at i and j indices
            cur = nums1[i] * nums2[j] + dfs(i+1, j+1, True)
            # 2. skip number from nums1
            skip_nums1 = dfs(i+1, j, picked)
            # 3. skip number from nums2
            skip_nums2 = dfs(i, j+1, picked)
            # return the max
            cache[(i, j, picked)] = max(cur, skip_nums1, skip_nums2)

            return cache[(i, j, picked)]
        return dfs(0, 0, False)
        """

        # DP: Bottom-up
        """
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                prod = nums1[i] * nums2[j]
                res = prod + max(0, dp[i+1][j+1])
                skip_nums1 = dp[i+1][j]
                skip_nums2 = dp[i][j+1]

                dp[i][j] = max(res, skip_nums1, skip_nums2)

        return dp[0][0]
        """

        # DP: Bottom-up, space optimized
        m, n = len(nums1), len(nums2)
        dp = [float('-inf')] * (n+1)

        for i in range(m-1, -1, -1):
            newDp = [float('-inf')] * (n+1)
            for j in range(n-1, -1, -1):
                prod = nums1[i] * nums2[j]
                res = prod + max(0, dp[j+1])
                skip_nums1 = dp[j]
                skip_nums2 = newDp[j+1]

                newDp[j] = max(res, skip_nums1, skip_nums2)
            dp = newDp
        return dp[0]