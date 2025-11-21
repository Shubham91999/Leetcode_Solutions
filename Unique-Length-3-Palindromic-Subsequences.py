class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Backtracking + helper to check palindrome
        # Gives TLE 
        """
        pal_set = set()

        def backtrack(i: int, curStr: str) -> None:
            if len(curStr) == 3:
                if self.isPalindrome(curStr):
                    pal_set.add(curStr)
                    return 
            if i == len(s):
                return

            # Skipping the current character
            backtrack(i+1, curStr)

            # Adding the current character
            backtrack(i+1, curStr+s[i])

        backtrack(0, '')
        return len(pal_set)

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    """
        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            ans += len(between)

        return ans
