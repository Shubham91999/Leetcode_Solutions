class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            print(str(x))
            x_str = str(x)
            l = 0
            r = len(x_str) - 1
            while l <= r:
                if x_str[l] != x_str[r]:
                    return False
                print(l, r)
                print("/n")
                l += 1
                r -= 1
            return True
            #return True