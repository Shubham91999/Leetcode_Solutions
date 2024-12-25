class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. Brute Force Approach
        # Return empty string, if target string is empty
        if t == '':
            return ''

        # Frequency counter for target string
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")

        # first for loop for i pointer, iterating on main string s
        for i in range(len(s)):
            countS = {}
            # Second for loop for taking substrings of main string and keeping counter
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True

                # Comparing counts in both freq counters
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break

                if flag and (j-i+1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ""
        """

        # Sliding Window Approach with o(n)
        if t == "":
            return ""
        
        countT = {} 
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""