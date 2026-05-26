class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26
        count = 0
        for char in list(word):
            index = ord(char)
            if index <= 96:
                upper[index - ord('A')] = True
            else:
                lower[index - ord('a')] = True

        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count
 
