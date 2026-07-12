class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_set = set(arr)
        num_order = {}

        for i, num in enumerate(sorted(arr_set)):
            num_order[num] = i+1
        
        res = []
        for num in arr:
            res.append(num_order[num])


        return res