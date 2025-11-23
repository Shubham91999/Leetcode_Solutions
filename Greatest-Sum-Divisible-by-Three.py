from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 1. Greedy
        # Time: O(n log n), Space: O(n)
        """

        # Group of elements with remainder == 0
        a = [x for x in nums if x % 3 == 0]

        # Group of elements with remainder == 1
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)

        # Group of elements with remainder == 2
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0

        lb, lc = len(b), len(c)

        for cntb in [lb-2, lb-1, lb]:
            if cntb >= 0:
                for cntc in [lc-2, lc-1, lc]:
                    if cntc >= 0 and (cntb-cntc) % 3 == 0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))

        return ans + sum(a)

        """

        # 2. DP 
        f = [0, -float('inf'), -float('inf')] # Max sum for remainders [0, 1, 2]

        for num in nums:
            new_f = f[:] # Creating copy of current max sums

            cur_mod = num % 3

            for i in range(3):
                new_remainder = (i + cur_mod) % 3

                # Storing max sum -> comparing with previous max sum and current sum
                new_f[new_remainder] = max(new_f[new_remainder], f[i] + num)

            f = new_f

        return f[0]










