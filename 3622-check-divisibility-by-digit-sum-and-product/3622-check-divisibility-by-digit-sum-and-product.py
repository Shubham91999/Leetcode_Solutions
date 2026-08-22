"""
- Initialize variables for digitSum and digitProduct
- use arithmetic calculation to select a single digit in number 
    - 99
    - Mod number by 10 to get the digit at one's place -> 9
    - Divide the number by 10 -> 9
    - Repeat till the division is 0
- Add it to digitSum
- Multiple with digitProduct
- Check if number of divisible by (digitSum + digitProduct)
    - if yes, return True
    - False otherwise
"""

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProduct = 1
        num = n

        while num:
            digit = num % 10 
            digitSum += digit
            digitProduct *= digit
            num = num // 10
        
        # print(digitSum)
        # print(digitProduct)
        if n % (digitSum + digitProduct) == 0:
            return True
        return False

        
        