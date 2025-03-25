class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Brute Force
        # res = {}
        # unique = set(nums)

        # for num in unique:
        #     res[num] = nums.count(num)
        # res = dict(sorted(res.items(), key= lambda item: item[1], reverse=True)[:k])
        # #print(list(res.keys()))
        # return list(res.keys())

        # 2. Using MinHeap
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # 3. Modified Bucket Sort
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # Hashmap of num : count pairs
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # Frequency list with list of numbers at their count = index in freq position
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            
        




