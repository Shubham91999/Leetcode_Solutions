class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Brute Force
        # while len(stones) > 1:
        #     stones.sort()
        #     curr = stones.pop() - stones.pop()
        #     if curr:
        #         stones.append(curr)
        # return stones[0] if stones else 0

        # 2. Using MaxHeap
        # stones = [-x for x in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
        #     if second > first:
        #         heapq.heappush(stones, first - second)
        # return abs(stones[0]) if stones else 0 

        # 3. Bucket Sort
        """ 
        Getting max stone weight to 
        create bucket array where bucket[i] 
        stores the count of stones of wieght i
        """
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones: # stones = [2, 7, 4, 1, 8, 1]
            bucket[stone] += 1 # bucket = [0, 2, 1, 0, 1, 0, 0, 1, 1] 
        # Initiliazing first and second heaviest stone
        first = second = maxStone # 8 in this case
        while first > 0:
            if bucket[first] % 2 == 0: # If count of stones with max weight is even, they'll cancel out each other, no need to look for second heaviest weight
                first -= 1 # Decrementing the heaviest stone weight
                continue
            # Getting the second heaviest as max weight count is odd, leaving one stone for further comparison
            j = min(first-1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1 # Decreasing value of j to find next heaviest possible stone
            # if no second heaviest stone found, return first as its the last remaining stone
            if j == 0:
                return first
            # if second stone found, reduce bucket counts, smash stones add it to bucket, update first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first-second] += 1
            first = max(first-second, second)
        return first

        


        