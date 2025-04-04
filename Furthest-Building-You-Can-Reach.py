class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 1. Using MinHeap
        # ladder_allocations = []  # Minheap
        # for i in range(len(heights)-1):
        #     climb = heights[i+1] - heights[i] # Difference between current and next building
        #     if climb <= 0: # if next building is lesser in height, no change
        #         continue
        #     heapq.heappush(ladder_allocations, climb) # if greater, add climb in heap
        #     if len(ladder_allocations) <= ladders: # if heap size is less than number of ladders
        #         continue
        #     # if heap size becomes greater than number of ladders, 
        #     # subtract the top (min climb) of heap from bricks, automatically increading the number of ladders remaining
        #     bricks -= heapq.heappop(ladder_allocations)
        #     # while subtracting, if number of bricks become less than 0, 
        #     # return current position as no next climb possible, heap is already size of ladders so no ladders remaining 
        #     if bricks < 0:
        #         return i
        # return len(heights) - 1

        # 2. Using MaxHeap
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heights)-1
  





















                
