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
        # Edge Case
        if len(t) == 0:
            return ""

        # Two hashmaps to maintain count of characters
        countT = defaultdict(int)
        window = defaultdict(int)

        # Intializing countT, as it will never change
        for c in t:
            countT[c] += 1

        have = 0            # Currently satisfying matches
        need = len(countT)  # Need to satisfy 

        res = [-1, -1]          # Initializing l and r pointers as -1
        resLen = float('inf')   # Minimum length of substring initializing at max integer
        l = 0                    # left pointer

        # Slinding window part
        for r in range(len(s)):
            c = s[r]  # Added to our current window, so incrementing the count
            window[c] += 1

            """
            After adding char in window, 
            we will check if it we need that character (it is present in t)
            and the count of char in window matches count of char in t string

            If it matches, that means we have one more match 
            """
            if c in countT and countT[c] == window[c]:
                have += 1

            """
            After updating have, we need to check if it matches the need count
            if matches and current window has length lesser than the previously found min,
            1) we will update l and r pointers 
            2) Update min length
            3) Shorten window from left
            4) Window changed, so update have count based on condition
            5) update l pointer to remove char at left from window
            """

            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        # Once the r pointer reaches end, res will be having l and r pointers giving minimum size window
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""