class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        total = 0
        concatenated = []
        for num in str(n):
            if num != '0':
                concatenated.append(num)
                total += int(num)
                

        res = int(''.join(concatenated)) * total
        return res


        