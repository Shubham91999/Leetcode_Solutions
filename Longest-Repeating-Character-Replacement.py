class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        1. Brute Force Approach
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j-i+1) - maxf <= k:
                    res = max(res, j-i+1)
        return res"""
 

        """
        2. Sliding Window Approach
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res
        """

        count, res = {}, 0
        l, maxf = 0, 0
         
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res