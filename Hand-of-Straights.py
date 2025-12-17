from typing import List
from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if hand can be divided equally by groupSize
        if len(hand) % groupSize:
            return False

        # frequency counter
        count = defaultdict(int)
        for h in hand:
            count[h] += 1

        # building minheap
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # iterate while there are elements in minheap
        while minHeap:
            start = minHeap[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

