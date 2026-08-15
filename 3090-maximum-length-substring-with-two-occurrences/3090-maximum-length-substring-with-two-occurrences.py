class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        res = 0
        for right, c in enumerate(s):
            ch = ord(c) - ord("a")
            count[ch] += 1
            while count[ch] > 2:
                ch2 = ord(s[left]) - ord("a")
                count[ch2] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res