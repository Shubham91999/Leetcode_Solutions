class KthLargest:
    # 1. MinHeap 
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # Initializing minHeap with nums list
        self.k = k # Kth largest elements
        
        heapq.heapify(self.minHeap) # Heapify to make it heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
 
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # If heap doesnt have k values, then no need to pop, we'll just add the new val
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

    # 2. Brute Force / Sorting
    # def __init__(self, k: int, nums: List):
    #     self.k = k
    #     self.arr = nums

    # def add(self, val: int)-> int:
    #     self.arr.append(val)
    #     self.arr.sort()
    #     return self.arr[len(self.arr) - self.k]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)