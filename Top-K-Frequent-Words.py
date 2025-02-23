# class HeapItem:
#     def __init__(self, word: str, count: int) -> None:
#         self.word = word
#         self.count = count

#     def __lt__(self, to_compare) -> bool:
#         if self.count == to_compare.count:
#             return self.word > to_compare.word
#         return self.count < to_compare.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # word_counts = collections.Counter(words)

        # heap = []

        # for word, count in word_counts.items():
        #     item = HeapItem(word, count)

        #     if len(heap) < k:
        #         heapq.heappush(heap, item)
        #     else:
        #         if item > heap[0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, item)
        # res = []
        # while k:
        #     cur = heapq.heappop(heap)
        #     res.append(cur.word)

        #     k -= 1
        # return list(reversed(res))

        # Optimal
        app = collections.Counter(words)
        h = [(v,k) for k,v in app.items()]
        h.sort(key= lambda x: (-x[0], x[1]))
        h = [x[1] for x in h][:k]
        return h

    

            
        