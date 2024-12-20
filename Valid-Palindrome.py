class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        1. Reverse String
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        """

        """
        2. Two Pointer Approach
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        #print(s)
        i, j = 0, len(s)-1
        #print(i, j)
        for i in range(len(s)-1):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        """

    # 3. Two Pointer Approach (Optimal without using library function)
        l, r = 0, len(s) - 1
         
        while l < r:

            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def alphaNum(self, c):
        return(
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )



        



