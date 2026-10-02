class Solution:
    """
    Function will receive number n of pairs to be generated using parenthesis
    Return List of valid combinations
    """
    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []

    #     # Function to check if the string is valid combination
    #     def valid(s: str) -> bool:
    #         open = 0  # Maintain count of open brackets
    #         for c in s:
    #             if c == '(':
    #                 open += 1  # Increment if opening parenthesis found
    #             else: 
    #                 open -= 1  # Decrement if closing parenthesis found
    #             if open < 0:   # Return False for invalid combination
    #                 return False
    #         return open == 0   # Return True for valid combination

    #     # Function to create combinations
    #     def dfs(s: str) -> str:
    #         # If length of combination is even, call valid function to check 
    #         if len(s) == n * 2:
    #             # If combination is even and valid, add to res list
    #             if valid(s):  
    #                 res.append(s)
    #             return

    #         dfs(s + '(')  # Generating combination by adding (
    #         dfs(s + ')')  # Generating combination by adding )
    #         return res

    #     dfs("")  # Starting dfs with empty string
    #     return res

    # 
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return 

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

        