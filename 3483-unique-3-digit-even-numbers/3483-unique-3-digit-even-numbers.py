class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for digit in digits:
            count[digit] += 1

        res = 0

        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):

                    if count[i] == 0 or count[j] == 0 or count[k] == 0:
                        continue

                    # Same digit cannot be used more times than available
                    if i == j == k:
                        if count[i] < 3:
                            continue
                    elif i == j:
                        if count[i] < 2:
                            continue
                    elif i == k:
                        if count[i] < 2:
                            continue
                    elif j == k:
                        if count[j] < 2:
                            continue

                    res += 1

        return res