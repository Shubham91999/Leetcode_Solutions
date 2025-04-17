class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Brute Force: Check with set of current substring
        substrings = []
        maxSub = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.append(s[i:j])
        for s in substrings:
            if len(s) == len(set(s)):
                maxSub = max(maxSub, len(s))
        return maxSub
        '''

        """
        2. Brute Force with char set
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
        """

        # 3. Sliding Window
        # charSet = set() # Set to store and compare unique chars
        # l = 0  # Left Pointer initialized at 0
        # res = 0 # Store max length

        # for r in range(len(s)):  # Updating r from 0 to len(s)
        #     while s[r] in charSet: # Checking if current char is already in set
        #         charSet.remove(s[l]) # If found, delete chars from left pointer till current to remove duplicate element
        #         l += 1
        #     charSet.add(s[r]) # Adding current char
        #     window_size = r - l + 1  # Calculating current window size
        #     res = max(res, window_size) # Getting max 
        # return res

        # 4. Sliding Window Optimal with Dictionary
        map = {} # char -> index
        l, res = 0, 0

        for r in range(len(s)): # R will iterate over all the chars starting from 0 to len(nums)
            if s[r] in map: # If found in dict, move left pointer to one step after the previous occurence of that char
                l = max(map[s[r]]+1, l)
            
            # If not found, add char in dictionary with its index
            map[s[r]] = r
            res = max(res, r - l + 1)

        return res




