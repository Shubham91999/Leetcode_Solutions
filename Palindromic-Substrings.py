class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1. Expand around center
        """
        # maintaining count
        res = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
        """
        def helper(l: int, r: int) -> int:
            cur = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur += 1
                l -= 1
                r += 1
            return cur

        # Optimal 
        res = 0

        for i in range(len(s)):
            res += helper(i, i)
            res += helper(i, i+1)

        return res

    

