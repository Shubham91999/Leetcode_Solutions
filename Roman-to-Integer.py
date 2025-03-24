class Solution:
    def romanToInt(self, s: str) -> int:
        # s = s.replace("IV", "IIII")
        # s = s.replace("IX", "IIIIIIIII")
        # s = s.replace("XL", "XXXX")
        # s = s.replace("XC", "XXXXXXXXX")
        # s = s.replace("CD", "CCCC")
        # s = s.replace("CM", "CCCCCCCCC")
        # print(s)
        # count = 0
        # for i in s:
        #     if i == "I":
        #         count += 1
        #     elif i == "V":
        #         count += 5
        #     elif i == "X":
        #         count += 10
        #     elif i == "L":
        #         count += 50
        #     elif i == "C":
        #         count += 100
        #     elif i == "D":
        #         count += 500
        #     elif i == "M":
        #         count += 1000
        # print(count)
        # return count

        # res = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }

        # s = s.replace('IV', 'IIII')
        # s = s.replace('IX', 'VIIII')
        # s = s.replace('XL', 'XXXX')
        # s = s.replace('XC', 'LXXXX')
        # s = s.replace('CD', 'CCCC')
        # s = s.replace('CM', 'DCCCC')
        # cnt = 0
        # for c in s:
        #     cnt += res[c]
        # #print(cnt)
        # return cnt

        # 2. Reverse pass
        res = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = res[s[-1]] #res.get(s[-1])
        print(res[s[-1]])
        for i in reversed(range(len(s)-1)):
            if res[s[i]] < res[s[i+1]]:
                total -= res[s[i]]
            else:
                total += res[s[i]]
        return total










