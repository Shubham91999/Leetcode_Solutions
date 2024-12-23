class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        substrings = []
        maxSub = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.append(s[i:j])
        for s in substrings:
            if len(s) == len(set(s)):
                maxSub = max(maxSub, len(s))
        return maxSub
        """

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

        """
        3. Sliding Window Approach
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l +1)
        return res
        """

        # 4. Optimal Sliding Window
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

