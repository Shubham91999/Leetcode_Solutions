class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        def recursive(curr: List[int]) -> List[int]:
            if len(curr) == 1:
                return curr

            res = []
            for i in range(len(curr)-1):
                res.append((curr[i]+curr[i+1])%10)

            return recursive(res)


        return recursive(nums)[0]

            

        