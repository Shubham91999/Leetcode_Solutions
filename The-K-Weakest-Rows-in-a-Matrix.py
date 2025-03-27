class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for index, num in enumerate(mat):
            count_ones = num.count(1)
            heapq.heappush(heap, (count_ones, index))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


            

