class Solution:
    def calculate(self, s: str) -> int:
        cur, res = 0, 0  # Current number and result
        sign = 1  # 1 -> addition / -1 -> subtraction

        stack = [] # To track current result and operation before entering ()

        for char in s:
            # Check for digit
            if char.isdigit():
                cur = cur * 10 + int(char)  # Multiply by 10 for cases like 334 + 221
            # Check for sign
            elif char in "+-":
                res += sign * cur  # Adding product of sign and cur with res
                # As we found sign, we need to reset the sign 
                sign = 1 if char == '+' else -1
                cur = 0 # Resetting to 0 as we may find next int after operation sign
            # Check for (, opening parantheses
            elif char == "(": 
                # Appending current res and sign in stack to preserve current state
                stack.append(res)
                stack.append(sign)
                # Resetting cur and res values to simulate new iteration of function
                res = 0
                sign = 1
            elif char == ")":
                res += sign * cur # Adding integer present before right parantheses
                res *= stack.pop() # First pop -> sign 
                res += stack.pop() # Second pop -> previous result
                cur = 0
        return res + sign * cur

