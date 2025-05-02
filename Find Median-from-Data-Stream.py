class MedianFinder:
    # 1. Brute Force with Bisect
    # def __init__(self):
    #     self.nums = []

    # def addNum(self, num: int) -> None:
    #     bisect.insort(self.nums, num) # Same as insort_right -> add num in sorted order, in right position for eqaul num

    # def findMedian(self) -> float:
    #     n = len(nums)
    #     mid = n // 2
    #     if n % 2 == 1:
    #         return self.nums[mid]
    #     else:
    #         return self.nums[mid-1] + self.nums[]

    # 2. Two Heaps
    def __init__(self):
        self.small, self.large = [], [] # small -> MaxHeap, so top will hold max element, large -> MinHeap, so top will hold min element

    def addNum(self, num: int) -> None:
        # Initially adding new num to small heap
        heapq.heappush(self.small, -1 * num) # Negating num to maintain maxheap

        # Checking all nums in small heap are smaller or equal to every num in large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small) # Negating to get original value
            heapq.heappush(self.large, val)  # Adding original value to max heap

        # Now, maintaining equal distribution, length of heaps (Uneven size)
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) / 2


