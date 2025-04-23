class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. Brute Force with creating all strings with length n*2, checking for valid strings
        # res = []

        # def valid(s: str):
        #     open = 0
        #     for c in s:
        #         if c == '(':
        #             open += 1
        #         else:
        #             open -= 1
        #         if open < 0:
        #             return False
        #     return not open

        # def dfs(s : str):
        #     if n*2 == len(s):
        #         if valid(s):
        #             res.append(s)
        #     dfs(s + '(')
        #     dfs(s + ')')
        # dfs('')
        # return res

        # 2. Backtracking 
        stack = [] # maintains the current char list
        res = [] # maintaines the list of valid strings

        def backtrack(openN, closeN):
            # only add open paranthesis if open < n
            # only add close paranthesis if closed < open
            # string is valid if open == close == n

            # Checking base case, 
            if openN == closeN == n: # Open and close counters matching given n, it means string is valid
                res.append(''.join(stack))
                return 

            if openN < n:
                stack.append('(') # Count of open paranthesis is less than given limit n
                backtrack(openN + 1, closeN) # added open paranthesis, so incrementing the open count
                stack.pop() 

            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res




