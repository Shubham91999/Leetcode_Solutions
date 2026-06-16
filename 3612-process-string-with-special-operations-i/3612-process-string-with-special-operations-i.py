class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.islower() and 97 <= ord(c) <= 122:
                res.append(c)
            elif c == '*':
                if res:
                    del res[-1]
            elif c == '#':
                res = res + res
            elif c == '%':
                res.reverse()
            # print(res)

        return ''.join(res)