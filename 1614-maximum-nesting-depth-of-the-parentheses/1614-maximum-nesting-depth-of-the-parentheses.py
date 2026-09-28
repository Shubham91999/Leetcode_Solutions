class Solution:
    def maxDepth(self, s: str) -> int:
        depth = []
        res = 0
        for c in s:
            if c == '(':
                depth.append('(')
            elif c == ')':
                res = max(res, len(depth))
                depth.pop()
        return res
