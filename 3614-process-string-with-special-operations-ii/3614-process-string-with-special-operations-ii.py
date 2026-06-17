class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for c in s:
            # remove last character
            if c == '*':
                if length:
                    length -= 1
            # duplicates the string, cutting length by half
            elif c == '#':
                length *= 2
            # no change in length, as it just reverses the result
            elif c == '%':
                pass
            else:
                # letter appended, increasing the length by 1
                length += 1
        # required position is greater than resultant length
        if k + 1 > length:
            return '.'
        for c in reversed(s):
            if c == '*':
                length += 1
            elif c == '#':
                if k + 1 > (length + 1) // 2:
                    k -= length // 2
                length = (length + 1) // 2
            elif c == '%':
                k = length - k - 1
            else:
                if k + 1 == length:
                    return c
                length -= 1
        return "."

                