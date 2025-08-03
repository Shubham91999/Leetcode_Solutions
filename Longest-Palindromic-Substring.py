class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. Brute Force
        # res = ''
        # resLen = 0
        # n = len(s)
        # for i in range(n):
        #     for j in range(i, n):
        #         l, r = i, j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
        #         if l >= r and resLen < (j-i+1):
        #             res = s[i:j+1]
        #             resLen = j-i+1
        # return res

        # 2. Two Pointers
        res = ''
        resLen = 0
        n = len(s)
        for i in range(n):
            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # Even Length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res