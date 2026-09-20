class Solution:
    def reverseDegree(self, s: str) -> int:
            return sum((26 - (ord(char) - ord('a'))) * (i + 1) for i, char in enumerate(s))
