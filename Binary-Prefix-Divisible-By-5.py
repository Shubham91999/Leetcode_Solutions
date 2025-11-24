class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # 1. Brute force
        """
        cur = ''
        res = []

        for num in nums:
            cur += str(num)
            cur_num = int(cur, 2)
            print(cur_num)
            if cur_num % 5 == 0:
                res.append(True)
                continue
            res.append(False)

        return res
        """

        # 2. Optimized
        res = []
        cur = 0
        
        for num in nums:
            cur = (cur * 2 + num) % 5
            res.append(cur == 0)

        return res

