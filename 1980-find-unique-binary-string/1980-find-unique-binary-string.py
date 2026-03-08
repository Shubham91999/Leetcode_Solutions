class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        total = []
        def generate_binary(n, current=""):
            nonlocal total
            if len(current) == n:
                total.append(current)
                return 

            generate_binary(n, current + '0')

            generate_binary(n, current + '1')

        generate_binary(len(nums[0]))

        for s in total:
            if s not in nums:
                return s

        return ''
        