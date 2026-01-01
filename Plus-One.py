from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. Brute Force
        """
        s = ''
        for num in digits:
            s += str(num)
        s = int(s)
        s = s + 1
        s = str(s)
        res = []
        for c in s:
            res.append(int(c))
        return res
        """

        # 2. Optimal Solution

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits