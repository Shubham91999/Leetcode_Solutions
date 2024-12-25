class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Brute Force Approach
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        return s == ''
        """
        # 2. Using Stack
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[", 
            "}" : "{"
        }

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return  len(stack) == 0        