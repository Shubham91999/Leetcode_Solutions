class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge Case
        if '0' in [num1, num2]:
            return '0'

        # Resultant array
        res = [0] * (len(num1) + len(num2))

        # Reverse the input numbers
        num1, num2 = num1[::-1], num2[::-1]

        # Loop for multiplication of single digits
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Current multiplication
                cur_result = int(num1[i]) * int(num2[j])
                # Adding current result to previous o/p at same array index
                res[i+j] += cur_result
                # Handling carry
                res[i+j+1] += res[i+j] // 10
                # Handling two digits at current index
                res[i+j] = res[i+j] % 10

        # Reversing res array
        res = res[::-1]

        # Trimming leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = res[beg:]

        # Converting to str objects
        res = map(str, res)

        return ''.join(res)