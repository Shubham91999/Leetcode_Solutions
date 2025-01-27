class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "IIIIIIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "XXXXXXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "CCCCCCCCC")
        print(s)
        count = 0
        for i in s:
            if i == "I":
                count += 1
            elif i == "V":
                count += 5
            elif i == "X":
                count += 10
            elif i == "L":
                count += 50
            elif i == "C":
                count += 100
            elif i == "D":
                count += 500
            elif i == "M":
                count += 1000
        print(count)
        return count