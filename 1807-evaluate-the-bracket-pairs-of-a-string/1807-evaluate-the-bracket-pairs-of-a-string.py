"""
- Create a hashmap of knowledge -> key:value pairs
- Get the keys from input string
- Replace keys with values from knowledge
- Return the resultant string
"""
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Converting knowledge array to hashmap for faster retrieval
        k_map = {}
        for key, val in knowledge:
            k_map[key] = val

        # Get the keys 
        l, r = 0, 0
        res = []
        in_bracket = False
        while r < len(s):
            # Char at r is (
            if s[r] == '(':
                in_bracket = True
                l = r
            # Char at r is )
            elif s[r] == ')':
                key = s[l+1:r]
                in_bracket = False
                if key in k_map:
                    res.append(k_map[key])
                else:
                    res.append('?')
            # Char at r is lowercase letter
            else:
                if not in_bracket:
                    res.append(s[r])
            r += 1

        return ''.join(res)

        
        