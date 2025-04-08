class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 1. Sorting
        # points.sort(key = lambda p: p[0]**2 + p[1]**2)
        # print(points[:k])
        # return points[:k]

        # 2. Using Max Heap
        maxHeap = [] 
        for x, y in points:
            dist = -(x ** 2 + y ** 2) # calculating distance from origin
            heapq.heappush(maxHeap, [dist, x, y]) # Maintaining heap based on calculated distance, appending with x, y
            if len(maxHeap) > k: # To maintain heap size to k
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res


