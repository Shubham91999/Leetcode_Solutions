class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # # Negate the stones to simulate max heap using heapq (which is a min-heap by default)
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # # Process the stones until at most one remains
        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
            
        #     # If the two stones are not the same, push the difference back into the heap
        #     if first != second:
        #         heapq.heappush(stones, first - second)

        # # If there's one stone left, return its negated value (to convert it back to positive)
        # return -stones[0] if stones else 0


        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1
        
        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first