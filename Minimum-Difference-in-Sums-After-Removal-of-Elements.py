class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3

        s = 0 # Store Sum
        pre = [0] * (m+1) # List to maintain sum of best n elements up to index i
        q1 = [] # Max-Heap with negated values
        for i, x in enumerate(nums[: n*2], 1):
            s += x
            heappush(q1, -x)
            if len(q1) > n:
                s -= -heappop(q1)
            pre[i] = s

        # Track suffix min sum of n largest elements using min-heap
        s = 0
        suf = [0] * (m+1) # Sum of n largest from nums[i:]
        q2 = []  # min-heap
        for i in range(m, n, -1):  # from m to n+1
            x = nums[i-1]
            s += x
            heappush(q2, x)
            if len(q2) > n:
                s -= heappop(q2)
            suf[i] = s

        # Try every split between pre[i] and suf[i] where i is in n, 2n
        return min(pre[i]-suf[i+1] for i in range(n, n*2+1))



        