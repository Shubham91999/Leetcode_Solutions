class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n: int) -> int:
            x = n
            num = 0
            while x:
                digit = x % 10
                x = x // 10
                num = num * 10 + digit 
            return num

        return abs(n - reverse(n))

    