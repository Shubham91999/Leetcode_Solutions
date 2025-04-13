from heapq import heappush, heappop

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        maxprofit = 0
        heap = []
        
        for start, end, profit in jobs:
            while heap and start >= heap[0][0]:
                maxprofit = max(maxprofit, heap[0][1])
                heappop(heap)
            
            combined_job = (end, profit + maxprofit)
            
            heappush(heap, combined_job)
            
        while heap:
            maxprofit = max(maxprofit, heap[0][1])
            heappop(heap)
        
        return maxprofit
        