class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Frequency Count approach
        # freq = [0] * 26 # Frequency array to store count of 26 alphabets
        # for char in s:
        #     freq[ord(char) - ord('a')] += 1 # Incrementing counter if based in char
        # max_freq = max(freq) 
        # if max_freq > (len(s) + 1) // 2: # If any character appears more than half of len of s + 1, it is impossible to reorganize them
        #     return ""
        
        # res = [] # List to store result
        # while len(res) < len(s):  # Loop till lenght of result is less than given string
        #     # we will append two chars in one iteration
        #     # Append char with max frequency
        #     maxIDx = freq.index(max(freq)) # got max freq
        #     char = chr(maxIDx + ord('a'))  # got character based on freq using chr method
        #     res.append(char) # appending first char

        #     freq[maxIDx] -= 1  # Decrement freq after appending
        #     if freq[maxIDx] == 0:  # if freq is equal to 0, continue to next iteration
        #         continue

        #     # Appending char with second most freq
        #     tmp = freq[maxIDx]
        #     freq[maxIDx] = float("-inf") # temporarily making freq of most freq -inf to get second most freq
        #     nextMaxIDx = freq.index(max(freq)) 
        #     char = chr(nextMaxIDx + ord('a'))
        #     res.append(char) # Appended second char

        #     freq[maxIDx] = tmp
        #     freq[nextMaxIDx] -= 1
        # return ''.join(res)

        # 2. Max-Heap
        freq_map = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in freq_map.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap) > 1:
            # Popping two most frequent chars
            cnt1, char1 = heapq.heappop(max_heap)
            cnt2, char2 = heapq.heappop(max_heap)

            res.extend([char1, char2])

            if -cnt1 > 1:
                heapq.heappush(max_heap, (cnt1+1, char1))
            if -cnt2 > 1:
                heapq.heappush(max_heap, (cnt2+1, char2))
            
        # if last pair remaining in heap
        if max_heap:
            cnt, char = heapq.heappop(max_heap)
            if -cnt > 1:
                return ""
            res.append(char)

        return ''.join(res)


        









