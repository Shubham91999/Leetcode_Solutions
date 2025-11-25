"""
k => positive integer
length of smallest positive integer (n) => n is divisible by k
n only contains digit 1 (0, 2-9 not allowed)

k = 1  => n = 1 => returning length i.e. 1
k = 2  => No integer with digit divisible by 2
k = 3  => n = 111 => returning length i.e. 3
k = 4  => No integer with digit divisible by 2

base case   - if k is even, return -1
            - if k is multiple of 5, return -1
            - 
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Handling base cases
        # Even K and multiples of 5
        if k % 2 == 0 or k % 5 == 0:
            return -1

        if k == 1:
            return 1

        remainder = 1
        length = 1

        while remainder != 0:
            remainder = (remainder * 10 + 1) % k
            length += 1

        return length

        

        