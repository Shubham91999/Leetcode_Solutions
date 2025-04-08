class MedianFinder:

    def __init__(self):
        # Defining two heaps
        self.small, self.large = [], []  # small heap should be max heap, top will be the greatest element
        # large heap will be minheap, top will hold minimum value
        

    def addNum(self, num: int) -> None:
        # Adding element in small heap first (multipying by -1 to make it max heap) 
        heapq.heappush(self.small, -1 * num)

        # Making sure every element in small heap is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]): # if both heaps present and top value of small heap is greater than top value of large 
            val = -1 * heapq.heappop(self.small) # Pop it from small heap and add to large
            heapq.heappush(self.large, val) # Large heap is min heap so no need of negative values, thus negating again to get orignal value

        # Handling uneven sizes
        if len(self.small) > len(self.large)+1: # if len of small heap is greater, pop top and add in large heap
            val = -1 * heapq.heappop(self.small) # negating to add original value in large 
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small)+1: # if len of large heap is greater, pop top and add in small heap with negated value
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): # addNum function will make sure both heaps have same lenght, if not then number of elements is odd
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()