class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in closeToOpen:
                # Closing paranthesis
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
