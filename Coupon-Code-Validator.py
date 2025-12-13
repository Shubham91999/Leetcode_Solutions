"""
- Coupon is valid only if:
    - contains alphanumeric chars and '_', no other special chars
    - business line in given business list
    - isActive -> True/true
- collect valid coupons
- sort:
    - business line (lexicographically)
    - coupon code (lexicographically)
- return sorted list of coupon codes


"""
import re
from collections import defaultdict
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        BUSINESS = ["electronics", "grocery", "pharmacy", "restaurant"]
        res = defaultdict(list)
        n = len(code)

        # Function to check valid coupon code
        def isValid(code: str) -> bool:
            if not code:
                return False
            return re.fullmatch(r'[A-Za-z0-9_]+', code) is not None

        # Iterating over all the coupons
        for i in range(n):
            # Collecting valid coupons
            if isValid(code[i]) and (businessLine[i] in BUSINESS) and isActive[i]:
                res[businessLine[i]].append(code[i])

        final = []
        # Sorting res dict
        for category in BUSINESS:
            if category in res:
                final.extend(sorted(res[category]))
        return final
        


        

            





        