class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Brute Force Approach
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('[]', '')
        #     s = s.replace('{}', '')
        # return len(s) == 0

        # 2. Using Stack
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s:
            # If current character is closing parantheses, check further 
            if c in closeToOpen:
                # If stack has elements and top of stack is matching with closing parantheses(current char's value in hashmap)
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # If current character is opening parantheses add it in stack
                stack.append(c)
        return len(stack) == 0 # Stack length 0 indicates parantheses matched and got popped

