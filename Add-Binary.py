class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        print(a)
        print(b)
        print(bin(a+b))
        result = str(bin(a+b))
        return result[2:]