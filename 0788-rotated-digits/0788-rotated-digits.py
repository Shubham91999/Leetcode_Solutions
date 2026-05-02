class Solution:
    def rotatedDigits(self, n: int) -> int:
        INVALID = {3, 4, 7}
        CHANGES = {2, 5, 6, 9}

        count = 0
        for x in range(1, n + 1):
            digits = (int(d) for d in str(x))
            valid, changed = True, False

            for d in digits:
                if d in INVALID:
                    valid = False
                    break
                if d in CHANGES:
                    changed = True

            if valid and changed:
                count += 1

        return count