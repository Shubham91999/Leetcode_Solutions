from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Result list
        res = []
        
        # Digits to char map
        digitsToChars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Helper function for backtracking 
        def backtrack(i: int, curStr: str) -> None:
            # Base Case
            if len(curStr) == len(digits):
                res.append(curStr)
                return 

            # Recurrence relation

            for c in digitsToChars[digits[i]]:
                backtrack(i+1, curStr+c)
 
        backtrack(0, '')
        return res