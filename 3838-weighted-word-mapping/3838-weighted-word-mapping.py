"""
- Loop through the words in words array
    - Loop through every character in word
    - Calculate the sum
    - result = sum modulo 26
    - 25 - result
    - Append character at 25 - result to res list
- Return list -> string
"""

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total = 0
            for char in word:
                index = ord(char) - ord('a')
                total += weights[index]
            # print(total)
            total = total % 26
            # print(total)
            index = 25 - total
            res.append(chr(index+97))
        return ''.join(res)

        