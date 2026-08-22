"""
- Get digits 
- Get sum of digits 
- Get product of digits 
- Check if number is divisible by both 
    - if yes, return true
    - else, return false
"""


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        listN = self.getDigits(n)
        digit_sum = 0
        digit_product = 1

        for num in listN:
            digit_sum += int(num)
            digit_product *= int(num)

        if n % (digit_sum + digit_product) == 0:
            return True

        return False

    def getDigits(self, n: int) -> List[int]:
        strN = str(n)
        return list(strN)

        